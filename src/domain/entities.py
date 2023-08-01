from dataclasses import asdict, dataclass, field
from typing import List, Optional


# 1st step
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

# 2nd
@dataclass(frozen=True)
class ArticleImage:
    url: str
    source: str


@dataclass
class CrawledTrend:
    keywords: List[str]
    texts: List[str] = field(default_factory=list)
    images: List[ArticleImage] = field(default_factory=list)

    @property
    def str_keywords(self):
        return ','.join(self.keywords)
