from dataclasses import asdict, dataclass, field
from datetime import date
from enum import StrEnum
from typing import List, Optional

from utils import create_url_path, reformat_yaml

# from utils import split_sentences


class TargetCountryCode(StrEnum):
    # The ranking is based on a combination of factors such as population, 
    # global influence, and national income levels.
    
    US = "US"  # United States
    JP = "JP"  # Japan
    DE = "DE"  # Germany
    GB = "GB"  # United Kingdom
    FR = "FR"  # France
    IN = "IN"  # India
    BR = "BR"  # Brazil
    RU = "RU"  # Russia
    IT = "IT"  # Italy
    CA = "CA"  # Canada
    KR = "KR"  # South Korea
    AU = "AU"  # Australia
    ES = "ES"  # Spain
    MX = "MX"  # Mexico
    NL = "NL"  # Netherlands
    CH = "CH"  # Switzerland
    TR = "TR"  # Türkiye
    SA = "SA"  # Saudi Arabia
    SE = "SE"  # Sweden
    ID = "ID"  # Indonesia
    BE = "BE"  # Belgium
    AR = "AR"  # Argentina
    ZA = "ZA"  # South Africa
    PL = "PL"  # Poland
    AT = "AT"  # Austria
    SG = "SG"  # Singapore
    UA = "UA"  # Ukraine
    TW = "TW"  # Taiwan
    NO = "NO"  # Norway
    IL = "IL"  # Israel
    MY = "MY"  # Malaysia
    VN = "VN"  # Vietnam
    HK = "HK"  # Hong Kong
    TH = "TH"  # Thailand
    DK = "DK"  # Denmark
    CL = "CL"  # Chile
    PH = "PH"  # Philippines
    CZ = "CZ"  # Czechia
    FI = "FI"  # Finland
    GR = "GR"  # Greece
    PT = "PT"  # Portugal
    IE = "IE"  # Ireland
    CO = "CO"  # Colombia
    RO = "RO"  # Romania
    NZ = "NZ"  # New Zealand
    HU = "HU"  # Hungary
    PE = "PE"  # Peru
    KE = "KE"  # Kenya
    NG = "NG"  # Nigeria



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
        return ', '.join(self.keywords)
    

    @classmethod
    def from_crawled_trend(cls, crawled_trend: CrawledTrend, translated_articles: Optional[List[str]]=None):
        return cls(
            keywords=crawled_trend.keywords,
            articles=translated_articles if translated_articles else crawled_trend.articles,
            images=crawled_trend.images
        )


### Step 4-5
class Language(StrEnum):
    BG = "BG"
    CS = "CS"
    DA = "DA"
    DE = "DE"
    EL = "EL"
    EN_GB = "EN-GB"
    EN_US = "EN-US"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FR = "FR"
    HU = "HU"
    ID = "ID"
    IT = "IT"
    JA = "JA"
    KO = "KO"
    LT = "LT"
    LV = "LV"
    NB = "NB"
    NL = "NL"
    PL = "PL"
    PT_BR = "PT-BR"
    PT_PT = "PT-PT"
    RO = "RO"
    RU = "RU"
    SK = "SK"
    SL = "SL"
    SV = "SV"
    TR = "TR"
    UK = "UK"
    ZH = "ZH"


    def __repr__(self):
        return self._value_

@dataclass
class QnA:
    question: str
    answer: str


@dataclass
class ArticleContent:
    title: str
    lead: str
    body1: str
    body2: str
    qna_list: List[QnA]
    language: Language


    def to_list(self):
        qna_list = []
        for qa in self.qna_list:
            qna_list.append(qa.question)
            qna_list.append(qa.answer)

        return [
            self.title,
            self.lead,
            self.body1,
            self.body2,
            *qna_list,
        ]
    
    @staticmethod
    def from_list(data: List[str], language: Language):
        if data is None:
            raise ValueError("Data cannot be None")

        qna = data[4:]
        qna_list = [
            QnA(
                qna[i], 
                qna[i+1]
            ) 
            for i in range(0, len(qna), 2)
        ]
        return ArticleContent(
            title=reformat_yaml(data[0]),
            lead=reformat_yaml(data[1]),
            body1=data[2],
            body2=data[3],
            qna_list = qna_list,
            language=language
        )



# from jinja2 import Template
# _sns_template = """{{ title }}

# {{ category }}

# {{ news_url }}

# {{ hashtags }}

# """
# SNS_TEMPLATE = Template(_sns_template)

@dataclass
class Article:
    NUM_PARAGRAPH_SENTENCES = 2

    category: str
    keywords: str
    contents: List[ArticleContent]
    images: List[ArticleImage]
    

    @property
    def url_safe_name(self) -> str:
        en_content = self.contents[0]
        return create_url_path(en_content.title)

    @property
    def hashtags(self) -> str:
        return ' '.join(['#' + item for item in self.keywords.split(',')])


    # @classmethod
    # def from_dto(cls, tct: TranslatedCrawledTrend, ai_data: Dict[str, str]):
    #     category = ai_data.pop('category')
        
    #     sentences: List[str] = split_sentences(ai_data['body'])

    #     if len(sentences) >= Article.NUM_PARAGRAPH_SENTENCES:
    #         paragraphs = [
    #             ' '.join(sentences[i:i+Article.NUM_PARAGRAPH_SENTENCES]) + '\n\n' 
    #             for i in range(0, len(sentences), Article.NUM_PARAGRAPH_SENTENCES)
    #         ]

    #         n = len(paragraphs) // 2
    #         body1 = ' '.join(paragraphs[:n])
    #         body2 = ' '.join(paragraphs[n:])
    #     else:
    #         body1 = ' '.join(sentences)
    #         body2 = ''

    #     qna_list= [QnA(question=qna['question'], answer=qna['answer']) for qna in ai_data['qna']]
    #     contents = [
    #         ArticleContent(
    #             title = reformat_yaml(ai_data['title']),
    #             lead = reformat_yaml(ai_data['lead']),
    #             body1 = body1,
    #             body2 = body2,
    #             qna_list = qna_list,
    #             language = Language.EN_US,
    #         )
    #     ]
    #     return cls(
    #         category=reformat_yaml(category),
    #         keywords=reformat_yaml(tct.str_keywords),
    #         contents=contents,
    #         images=tct.images
    #     )

    # def print_sns_articles(self, date) -> List[str]:
    #     for c in self.contents:
    #         news_url = f'https://wikitoday.io/{c.language}/news/{date}/{self.url_safe_name}'
    #         sns_post = SNS_TEMPLATE.render({
    #             'title': c.title,
    #             'category': self.category,
    #             'hashtags': self.hashtags,
    #             'news_url': news_url,
    #         })
    #         print(sns_post)
        

    def to_list(self) -> List[str]:
        """DeepL does not support json schema translation, so we need to pass it with an array typed texts"""
        english_content = self.contents[0]
        return english_content.to_list()

    
    def append_translation(self, from_list: List[str], language: Language):
        self.contents.append(
            ArticleContent.from_list(from_list, language)
        )


### Step 6

@dataclass
class Markdown:
    language: Language
    md: str

@dataclass
class Folder:
    today: date
    folder_name: str # create_url_path (max 20 char)
    mds: List[Markdown]

