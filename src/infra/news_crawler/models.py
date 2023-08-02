from dataclasses import dataclass
from typing import Optional

FALLBACK_SOURCE = "Google trends"

@dataclass
class NewsArticleDto:
    text: str
    img_url: Optional[str] = None
    img_src: str = FALLBACK_SOURCE
    language: Optional[str] = None

class NewsArticle:
    """
    Class representing a single news article containing all the information that news-please can extract.
    """
    authors = []
    date_download = None
    date_modify = None
    date_publish = None
    description = None
    filename = None
    image_url = None
    language = None
    localpath = None
    source_domain = None
    maintext = None
    text = None
    title = None
    title_page = None
    title_rss = None
    url = None

    def get_serializable_dict(self):
        """
        Get a serializable dict of the instance of this class.
        :return:
        """
        tmp = self.get_dict()
        tmp['date_download'] = str(tmp['date_download'])
        tmp['date_modify'] = str(tmp['date_modify'])
        tmp['date_publish'] = str(tmp['date_publish'])
        return tmp

    def get_dict(self):
        """
        Get the dict of the instance of this class.
        :return:
        """
        return {
            'authors': self.authors,
            'date_download': self.date_download,
            'date_modify': self.date_modify,
            'date_publish': self.date_publish,
            'description': self.description,
            'filename': self.filename,
            'image_url': self.image_url,
            'language': self.language,
            'localpath': self.localpath,
            'maintext': self.maintext,
            'source_domain': self.source_domain,
            'text': self.text,
            'title': self.title,
            'title_page': self.title_page,
            'title_rss': self.title_rss,
            'url': self.url
        }

    def to_dto(self, source: Optional[str]=None) -> NewsArticleDto:
        if not source:
            if len(self.authors) > 0:
                source = self.authors[0]
            elif self.source_domain:
                source = self.source_domain
            else:
                source = FALLBACK_SOURCE

        return NewsArticleDto(
            text= f'# Title:{self.title}\n\n# Lead:{self.description}\n\n# Body:{self.maintext}',
            img_src =source,
            img_url = self.image_url, 
            language = self.language,
        )


class ArticleCandidate:
    """This is a helpclass to store the result of an article after it was extracted. Every implemented extractor
    returns an ArticleCanditate as result.
    """
    url = None
    title = None
    description = None
    text = None
    topimage = None
    author = None
    publish_date = None
    extractor = None
    language = None
