from dataclasses import asdict, dataclass
from typing import List, Optional


@dataclass(frozen=True)
class ArticleMeta:
    url: str
    source: Optional[str] = None

@dataclass(frozen=True)
class Trend:
    query: str
    related_quries: List[str]
    articles: List[ArticleMeta]

    @property
    def keywords(self):
        return [self.query, *self.related_quries]

    @property
    def hrefs(self):
        return [a.url for a in self.articles]

    def as_dict(self):
        return asdict(self)

