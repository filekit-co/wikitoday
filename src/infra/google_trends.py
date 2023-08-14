import json
import logging
from dataclasses import dataclass, field
from typing import List, Optional

import httpx
from httpx import AsyncClient, Response

from domain.entities import GoogleTrend, TrendArticleMeta
from utils import generate_dataclass

GOOGLE_TRENDS_URL = "https://trends.google.com/trends/api/dailytrends"
logger = logging.getLogger(__name__)



@dataclass
class GoogleArticle:
    title: Optional[str] = None
    timeAgo: Optional[str] = None
    source: Optional[str] = None
    url: Optional[str] = None
    snippet: Optional[str] = None

    @property
    def dto(self):
        return TrendArticleMeta(
            url=self.url,
            source=self.source,
        )

@dataclass
class RelatedQuery:
    query: Optional[str] = None
    exploreLink: Optional[str] = None

@dataclass
class Title:
    query: Optional[str] = None
    exploreLink: Optional[str] = None


@dataclass
class TrendingDataEntry:
    NUM_MAX_ARTICLE = 2

    title: Optional[Title] = None
    formattedTraffic: Optional[str] = None
    relatedQueries: List[RelatedQuery] = field(default_factory=list)
    articles: List[GoogleArticle] = field(default_factory=list)
    shareUrl: Optional[str] = None


    def __post_init__(self):
        self.title = Title(**self.title)
        self.relatedQueries = [generate_dataclass(RelatedQuery, rq) for rq in self.relatedQueries]
        self.articles = [generate_dataclass(GoogleArticle, a) for a in self.articles]
        
    
    def to_dto(self) -> GoogleTrend:
        return GoogleTrend(
            query=self.title.query,
            related_quries=[r.query for r in self.relatedQueries if r.query],
            articles=[a.dto for a in self.articles if a.url][:TrendingDataEntry.NUM_MAX_ARTICLE]
        )


def _parse_trends(response: Response):
    try:
        start_index = response.text.index('{')
    except ValueError:
        logger.error(f"Invalid response: no json object found. Response: {response.text}")
        raise ValueError("Invalid response: no json object found")

    json_part = response.text[start_index:]

    try:
        loaded_json = json.loads(json_part)
    except json.JSONDecodeError:
        logger.error(f"Invalid response: not a json object. Response: {response.text}")
        raise ValueError("Invalid response: not a json object")

    try:
        trending_data = loaded_json['default']['trendingSearchesDays'][0]['trendingSearches']
    except KeyError:
        logger.error(f"Invalid response: expected keys not found. Response: {response.text}")
        raise ValueError("Invalid response: expected keys not found")


    if not trending_data:
        logger.error(f"No trending data available in the response. Response: {response.text}")
        raise ValueError("No trending data available in the response")

    return [generate_dataclass(TrendingDataEntry, entry) for entry in trending_data]


async def daily_trends(country:str, date: Optional[str]) -> List[GoogleTrend]:
    """_summary_

    Args:
        country (str): _description_
        date (Optional[str], optional): YYYYMMDD i.g. 20230801. Defaults to None.

    Returns:
        List[GoogleTrend]: google trends api response
    """
    meta_language='en-US'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://trends.google.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": f"https://trends.google.com/trends/trendingsearches/daily?geo={country}",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    }
    params = {
            'hl': meta_language,
            'geo': country,
            'ns': '15',
            }
    if date:
        params['ed'] = date
    
    async with httpx.AsyncClient() as client:
        r = await client.get(GOOGLE_TRENDS_URL, headers=headers, params=params)
        r.raise_for_status()
        trends = _parse_trends(r)
        only_three = [t.to_dto() for t in trends][:2]
        return only_three
