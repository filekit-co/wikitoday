import datetime
import urllib
from typing import Dict, List

from dotmap import DotMap

from domain.entities import ArticleImage, CrawledTrend, GoogleTrend
from infra.news_crawler.crawler import NewscrawlerItem, SimpleCrawler
from infra.news_crawler.extractor import Extractor
from infra.news_crawler.models import NewsArticle
from infra.news_crawler.storage import ExtractedInformationStorage


async def from_trends(trends: List[GoogleTrend], timeout=None) -> List[CrawledTrend]:
    urls = [
        href
        for trend in trends
        for href in trend.hrefs
    ]

    crawled_news = await _from_urls(urls, timeout=10.0)
    
    result = []
    for trend in trends:
        crawled_trend_data = {
            'keywords': trend.keywords,
            'articles': [],
            'images': [],
            'language': None,
        }

        for a in trend.articles:
            news = crawled_news.get(a.url, None)
            if not news:
                continue
            
            news_dto = news.to_dto(a.source)
            crawled_trend_data['articles'].append(news_dto.text)
            crawled_trend_data['images'].append(
                ArticleImage(url=news_dto.img_url, source=news_dto.img_src)
            )
            crawled_trend_data['language'] = news_dto.language
        
        # An article will be regenerated only if the crawled text data is existed.
        if crawled_trend_data['articles']:
            result.append(CrawledTrend(**crawled_trend_data))
    return result


async def _from_html(html, url=None, download_date=None, fetch_images=True) -> NewsArticle:
    """
    Extracts relevant information from an HTML page given as a string. This function does not invoke scrapy but only
    uses the article extractor. If you have the original URL make sure to provide it as this helps NewsPlease
    to extract the publishing date and title.
    :param html:
    :param url:
    :return:
    """
    extractor = Extractor()
    title_encoded = "".encode()
    if not url:
        url = ""
    # if an url was given, we can use that as the filename
    filename = urllib.parse.quote_plus(url) + ".json"
    item = NewscrawlerItem()
    item["spider_response"] = DotMap()
    item["spider_response"].body = html
    item["url"] = url
    item["source_domain"] = (
        urllib.parse.urlparse(url).hostname.encode() if url != "" else "".encode()
    )
    item["html_title"] = title_encoded
    item["rss_title"] = title_encoded
    item["local_path"] = None
    item["filename"] = filename
    item["download_date"] = download_date
    item["modified_date"] = None
    item = extractor.extract(item)
    tmp_article = ExtractedInformationStorage.extract_relevant_info(item)
    final_article = ExtractedInformationStorage.convert_to_class(tmp_article)
    return final_article

    
async def _from_urls(urls, timeout=None) -> Dict[str, NewsArticle]:
    """
    Crawls articles from the urls and extracts relevant information.
    :param urls:
    :param timeout: in seconds, if None, the urllib default is used
    :return: A dict containing given URLs as keys, and extracted information as corresponding values.
    """
    results = {}
    download_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if len(urls) == 0:
        pass
    elif len(urls) == 1:
        url = urls[0]
        html = await SimpleCrawler.fetch_url(url, timeout=timeout)
        if html:
            results[url] = await _from_html(html, url, download_date)
    else:
        results = await SimpleCrawler.fetch_urls(urls)
        for url, html in results.items():
            results[url] = await _from_html(html, url, download_date)
    return results
