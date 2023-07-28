import json
import locale
import logging
import re
import urllib.request as urllib2
from abc import ABCMeta, abstractmethod
from copy import deepcopy

from bs4 import BeautifulSoup
from dateutil.parser import parse
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
from lxml import html
from newspaper import Article
from readability import Document

from infra.news_crawler.cleaner import Cleaner
from infra.news_crawler.comparer.comparer import Comparer
from infra.news_crawler.models import ArticleCandidate


class AbstractExtractor:
    """Abstract class for article extractors.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self.name = None

    def _name(self):
        """Returns the name of the article extractor."""
        return self.name

    def _language(self, item):
        """Returns the language of the extracted article."""
        return None

    def _title(self, item):
        """Returns the title of the extracted article."""
        return None

    def _description(self, item):
        """Returns the description/lead paragraph of the extracted article."""
        return None

    def _text(self, item):
        """Returns the main text of the extracted article."""
        return None

    def _topimage(self, item):
        """Returns the top image of the extracted article."""
        return None

    def _author(self, item):
        """Returns the authors of the extracted article."""
        return None

    def _publish_date(self, item):
        """Returns the publish date of the extracted article."""
        return None

    def extract(self, item):
        """Executes all implemented functions on the given article and returns an
        object containing the recovered data.

        :param item: A NewscrawlerItem to parse.
        :return: ArticleCandidate containing the recovered article data.
        """

        article_candidate = ArticleCandidate()
        article_candidate.extractor = self._name()
        article_candidate.title = self._title(item)
        article_candidate.description = self._description(item)
        article_candidate.text = self._text(item)
        article_candidate.topimage = self._topimage(item)
        article_candidate.author = self._author(item)
        article_candidate.publish_date = self._publish_date(item)
        article_candidate.language = self._language(item)

        return article_candidate



class Extractor:
    """This class initializes all extractors and saves the results of them. When adding a new extractor, it needs to
    be initialized here and added to list_extractor.
    """

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.extractor_list = [
            NewspaperExtractor(),
            ReadabilityExtractor(),
            DateExtractor(),
            LangExtractor(),
        ]
        self.cleaner = Cleaner()
        self.comparer = Comparer()

    def extract(self, item):
        """Runs the HTML-response trough a list of initialized extractors, a cleaner and compares the results.

        :param item: NewscrawlerItem to be processed.
        :return: An updated NewscrawlerItem including the results of the extraction
        """

        article_candidates = []

        for extractor in self.extractor_list:
            article_candidate = extractor.extract(item)
            article_candidates.append(article_candidate)

        article_candidates = self.cleaner.clean(article_candidates)
        article = self.comparer.compare(item, article_candidates)

        item['article_title'] = article.title
        item['article_description'] = article.description
        item['article_text'] = article.text
        item['article_image'] = article.topimage
        item['article_author'] = article.author
        item['article_publish_date'] = article.publish_date
        item['article_language'] = article.language

        return item
    

class NewspaperExtractor(AbstractExtractor):
    """This class implements Newspaper as an article extractor. Newspaper is
    a subclass of ExtractorsInterface
    """

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.name = "newspaper"

    def _article_kwargs(self):
        return {}

    def extract(self, item):
        """Creates an instance of Article without a Download and returns an ArticleCandidate with the results of
        parsing the HTML-Code.

        :param item: A NewscrawlerItem to parse.
        :return: ArticleCandidate containing the recovered article data.
        """
        article_candidate = ArticleCandidate()
        article_candidate.extractor = self._name()

        article = Article('', **self._article_kwargs())
        # old version of newspaper2k
        # article.set_html(item['spider_response'].body)
        # new version
        article.download(input_html=item['spider_response'].body, title=item['html_title'].decode())
        article.parse()
        article_candidate.title = article.title
        article_candidate.description = article.meta_description
        article_candidate.text = article.text
        article_candidate.topimage = article.top_image
        article_candidate.author = article.authors
        if article.publish_date:
            try:
                article_candidate.publish_date = article.publish_date.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError as exception:
                self.log.debug('%s: Newspaper failed to extract the date in the supported format,'
                              'Publishing date set to None' % item['url'])
        article_candidate.language = article.meta_lang

        return article_candidate
    


class ReadabilityExtractor(AbstractExtractor):
    """This class implements Readability as an article extractor. Readability is
    a subclass of Extractors and newspaper.Article.

    """

    def __init__(self):
        self.name = "readability"

    def extract(self, item):
        """Creates an readability document and returns an ArticleCandidate containing article title and text.

        :param item: A NewscrawlerItem to parse.
        :return: ArticleCandidate containing the recovered article data.
        """

        doc = Document(deepcopy(item['spider_response'].body))
        description = doc.summary()

        article_candidate = ArticleCandidate()
        article_candidate.extractor = self._name
        article_candidate.title = doc.short_title()
        article_candidate.description = description
        article_candidate.text = self._text(item)
        article_candidate.topimage = self._topimage(item)
        article_candidate.author = self._author(item)
        article_candidate.publish_date = self._publish_date(item)
        article_candidate.language = self._language(item)

        return article_candidate
    


# to improve performance, regex statements are compiled only once per module
re_pub_date = re.compile(
    r'([\./\-_]{0,1}(19|20)\d{2})[\./\-_]{0,1}(([0-3]{0,1}[0-9][\./\-_])|(\w{3,5}[\./\-_]))([0-3]{0,1}[0-9][\./\-]{0,1})?'
)
re_class = re.compile("pubdate|timestamp|article_date|articledate|date", re.IGNORECASE)
class DateExtractor(AbstractExtractor):
    """This class implements ArticleDateExtractor as an article extractor. ArticleDateExtractor is
    a subclass of ExtractorInterface.
    """

    def __init__(self):
        self.name = "date_extractor"

    def _publish_date(self, item):
        """Returns the publish_date of the extracted article."""

        url = item['url']
        html = deepcopy(item['spider_response'].body)
        publish_date = None

        try:
            if html is None:
                request = urllib2.Request(url)
                # Using a browser user agent, decreases the change of sites blocking this request - just a suggestion
                # request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)
                # Chrome/41.0.2228.0 Safari/537.36')
                html = urllib2.build_opener().open(request).read()

            html = BeautifulSoup(html, "lxml")

            publish_date = self._extract_from_json(html)
            if publish_date is None:
                publish_date = self._extract_from_meta(html)
            if publish_date is None:
                publish_date = self._extract_from_html_tag(html)
            if publish_date is None:
                publish_date = self._extract_from_url(url)
        except Exception as e:
            # print(e.message, e.args)
            pass

        return publish_date

    def parse_date_str(self, date_string):
        try:
            date = parse(date_string)
            return date.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return None

    def _extract_from_url(self, url):
        """Try to extract from the article URL - simple but might work as a fallback"""

        # Regex by Newspaper3k  - https://github.com/codelucas/newspaper/blob/master/newspaper/urls.py
        m = re.search(re_pub_date, url)
        if m:
            return self.parse_date_str(m.group(0))
        return None

    def _extract_from_json(self, html):
        date = None
        try:
            script = html.find('script', type='application/ld+json')
            if script is None:
                return None

            data = json.loads(script.string)

            try:
                date = self.parse_date_str(data['datePublished'])
            except (Exception, TypeError):
                pass

            try:
                date = self.parse_date_str(data['dateCreated'])
            except (Exception, TypeError):
                pass
        except (Exception, TypeError):
            return None

        return date

    def _extract_from_meta(self, html):
        date = None
        for meta in html.findAll("meta"):
            meta_name = meta.get('name', '').lower()
            item_prop = meta.get('itemprop', '').lower()
            http_equiv = meta.get('http-equiv', '').lower()
            meta_property = meta.get('property', '').lower()

            # <meta name="pubdate" content="2015-11-26T07:11:02Z" >
            if 'pubdate' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name='publishdate' content='201511261006'/>
            if 'publishdate' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="timestamp"  data-type="date" content="2015-11-25 22:40:25" />
            if 'timestamp' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="DC.date.issued" content="2015-11-26">
            if 'dc.date.issued' == meta_name:
                date = meta['content'].strip()
                break

            # <meta property="article:published_time"  content="2015-11-25" />
            if 'article:published_time' == meta_property:
                date = meta['content'].strip()
                break
                # <meta name="Date" content="2015-11-26" />
            if 'date' == meta_name:
                date = meta['content'].strip()
                break

            # <meta property="bt:pubDate" content="2015-11-26T00:10:33+00:00">
            if 'bt:pubdate' == meta_property:
                date = meta['content'].strip()
                break
                # <meta name="sailthru.date" content="2015-11-25T19:56:04+0000" />
            if 'sailthru.date' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="article.published" content="2015-11-26T11:53:00.000Z" />
            if 'article.published' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="published-date" content="2015-11-26T11:53:00.000Z" />
            if 'published-date' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="article.created" content="2015-11-26T11:53:00.000Z" />
            if 'article.created' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="article_date_original" content="Thursday, November 26, 2015,  6:42 AM" />
            if 'article_date_original' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="cXenseParse:recs:publishtime" content="2015-11-26T14:42Z"/>
            if 'cxenseparse:recs:publishtime' == meta_name:
                date = meta['content'].strip()
                break

            # <meta name="DATE_PUBLISHED" content="11/24/2015 01:05AM" />
            if 'date_published' == meta_name:
                date = meta['content'].strip()
                break

            # <meta itemprop="datePublished" content="2015-11-26T11:53:00.000Z" />
            if 'datepublished' == item_prop:
                date = meta['content'].strip()
                break

            # <meta itemprop="datePublished" content="2015-11-26T11:53:00.000Z" />
            if 'datecreated' == item_prop:
                date = meta['content'].strip()
                break

            # <meta property="og:image" content="http://www.dailytimes.com.pk/digital
            # _images/400/2015-11-26/norway-return-number-of-asylum-seekers-to-pakistan-1448538771-7363.jpg"/>
            if 'og:image' == meta_property or "image" == item_prop:
                url = meta['content'].strip()
                possible_date = self._extract_from_url(url)
                if possible_date is not None:
                    return self.parse_date_str(possible_date)

            # <meta http-equiv="data" content="10:27:15 AM Thursday, November 26, 2015">
            if 'date' == http_equiv:
                date = meta['content'].strip()
                break

        if date is not None:
            return self.parse_date_str(date)

        return None

    def _extract_from_html_tag(self, html):
        # <time>
        for time in html.findAll("time"):
            datetime = time.get('datetime', '')
            if len(datetime) > 0:
                return self.parse_date_str(datetime)

            datetime = time.get('class', '')
            if len(datetime) > 0 and datetime[0].lower() == "timestamp":
                return self.parse_date_str(time.string)

        tag = html.find("span", {"itemprop": "datePublished"})
        if tag is not None:
            date_string = tag.get("content")
            if date_string is None:
                date_string = tag.text
            if date_string is not None:
                return self.parse_date_str(date_string)

        # class=
        for tag in html.find_all(['span', 'p', 'div'], class_=re_class):
            date_string = tag.string
            if date_string is None:
                date_string = tag.text

            date = self.parse_date_str(date_string)

            if date is not None:
                return date

        return None
    


class LangExtractor(AbstractExtractor):
    """This class implements LangDetect as an article extractor but it can only
    detect the extracted language (en, de, ...).

    """

    def __init__(self):
        self.name = "langdetect"
        self.langcode_pattern = re.compile(r'\b[a-zA-Z]{2}(?=([-_]|\b))')

    def _language(self, item):
        """Returns the language of the extracted article by analyzing metatags and inspecting the visible text
        with langdetect"""

        response = item['spider_response'].body
        try:
            root = html.fromstring(response)
        except ValueError:
            root = html.fromstring(response.encode("utf-8"))

        # Check for lang-attributes
        lang = root.get('lang')

        if lang is None:
            lang = root.get('xml:lang')

        # Check for general meta tags
        if lang is None:
            meta = root.cssselect('meta[name="language"]')
            if len(meta) > 0:
                lang = meta[0].get('content')

        # Check for open graph tags
        if lang is None:
            meta = root.cssselect('meta[property="og:locale"]')
            if len(meta) > 0:
                lang = meta[0].get('content')

        # Look for <article> elements and inspect the one with the largest payload with langdetect
        if lang is None:
            article_list = []
            for article in root.xpath('//article'):
                article_list.append(re.sub(r'\s+', ' ', article.text_content().strip()))
                longest_articles = sorted(article_list, key=lambda article: len(article), reverse=True)
                for article in longest_articles:
                    try:
                        lang = detect(article)
                    except LangDetectException:
                        continue
                    else:
                        break

        # Analyze the whole body with langdetect
        if lang is None:
            try:
                lang = detect(root.text_content().strip())
            except LangDetectException:
                pass

        # Try to normalize output
        if lang is not None:
            # First search for suitable locale in the original output
            matches = self.langcode_pattern.search(lang)
            if matches is not None:
                lang = matches.group(0)
            else:
                # If no match was found, normalize the original output and search again
                normalized = locale.normalize(re.split(r'\s|;|,', lang.strip())[0])
                matches = self.langcode_pattern.search(normalized)
                if matches is not None:
                    lang = matches.group(0)

        return lang
