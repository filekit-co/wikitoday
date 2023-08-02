from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional


### Step 1
@dataclass(frozen=True)
class TrendArticleMeta:
    url: str
    source: Optional[str] = None


@dataclass(frozen=True)
class GoogleTrend:
    query: str
    related_quries: List[str]
    articles: List[TrendArticleMeta]

    @property
    def keywords(self) -> List[str]:
        return [self.query, *self.related_quries]

    @property
    def hrefs(self):
        return [a.url for a in self.articles]
    
    def as_dict(self):
        return asdict(self)

### Step 2
@dataclass(frozen=True)
class ArticleImage:
    url: str
    source: str


@dataclass
class CrawledTrend:
    keywords: List[str]
    articles: List[str] = field(default_factory=list)
    images: List[ArticleImage] = field(default_factory=list)
    language: Optional[str] = None
    
    @property
    def is_en(self) -> bool:
        return self.language == 'en'


### Step 3
@dataclass
class TranslatedCrawledTrend:
    keywords: List[str]
    articles: List[str]
    images: List[ArticleImage]

    @property
    def str_keywords(self):
        return ','.join(self.keywords)


    @classmethod
    def from_crawled_trend(cls, crawled_trend: CrawledTrend, translated_articles: Optional[List[str]]=None):
        return cls(
            keywords=crawled_trend.keywords,
            articles=translated_articles if translated_articles else crawled_trend.articles,
            images=crawled_trend.images
        )


### Step 4
@dataclass
class QnA:
    question: str
    answer: str

@dataclass
class Article:
    title: str
    lead: str
    body: str
    qna: List[QnA]
    category: str

@dataclass
class LLMContent:
    keywords: List[str]
    article: Article
    images: List[ArticleImage]


    @classmethod
    def from_dto(cls, tct: TranslatedCrawledTrend, ai_data: Dict[str, str]):
        return cls(
            keywords=tct.keywords,
            article=Article(**ai_data),
            images=tct.images
        )
