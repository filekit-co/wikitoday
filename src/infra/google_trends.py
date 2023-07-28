import json
import logging
from dataclasses import asdict, dataclass
from typing import List, Optional

from httpx import AsyncClient, Response

GOOGLE_TRENDS_URL = "https://trends.google.com/trends/api/dailytrends"
logger = logging.getLogger(__name__)

@dataclass
class Image:
    newsUrl: Optional[str] = None
    source: Optional[str] = None
    imageUrl: Optional[str] = None

@dataclass
class Article:
    title: Optional[str] = None
    timeAgo: Optional[str] = None
    source: Optional[str] = None
    image: Optional[Image] = None
    url: Optional[str] = None
    snippet: Optional[str] = None

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
    title: Optional[Title] = None
    formattedTraffic: Optional[str] = None
    relatedQueries: Optional[List[RelatedQuery]] = None
    image: Optional[Image] = None
    articles: Optional[List[Article]] = None
    shareUrl: Optional[str] = None
    
    @property
    def as_dict(self):
        return asdict(self)    

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

    return [TrendingDataEntry(**entry) for entry in trending_data]


async def daily_trends(client: AsyncClient, country='US'):
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
    
    r = await client.get(GOOGLE_TRENDS_URL, headers=headers, params=params)
    trending_data_list: List[TrendingDataEntry] = _parse_trends(r)
    return trending_data_list