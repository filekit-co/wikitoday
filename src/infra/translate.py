import asyncio
import json
from typing import List

import httpx

from app.config import get_env
from domain.entities import CrawledTrend, TranslatedCrawledTrend
from src.app.exceptions import TranslationError

_cfg = get_env()
DEEPL_API_KEY = _cfg["DEEPL_API_KEY"]

async def translate_text(client: httpx.AsyncClient, texts: List[str], target_lang: str) -> dict:
    """
    EXAMPLE RESPONSE
    {
    "translations": [
        {
        "detected_source_language": "EN",
        "text": "Das ist der erste Satz."
        },
        {
        "detected_source_language": "EN",
        "text": "Das ist der zweite Satz."
        },
        {
        "detected_source_language": "EN",
        "text": "Dies ist der dritte Satz."
        }
    ]
    }
    """
    url = 'https://api-free.deepl.com/v2/translate'
    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'text': texts,
        'target_lang': target_lang
    }

    response = await client.post(url, headers=headers, data=json.dumps(data))
    translated = response.json()
    return [t['text'] for t in translated['translations']]


async def translate_texts(texts: List[str], target_lang: str = 'EN') -> List[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [translate_text(client, text, target_lang) for text in texts]
        return await asyncio.gather(*tasks)


async def translate_crawled_trends(trends: List[CrawledTrend], target_lang: str = 'EN') -> List[CrawledTrend]:
    en = [t for t in trends if t.is_en]
    others = [t for t in trends if not t.is_en]

    async with httpx.AsyncClient() as client:
        tasks = [translate_text(client, other.articles, target_lang) for other in others]
        responses = await asyncio.gather(*tasks)
        
        # TODO: error handling
        if len(others) != len(responses):
            raise TranslationError()
        
        return [
            TranslatedCrawledTrend.from_crawled_trend(ct, response) 
            for ct, response in zip(others, responses)
        ] + [TranslatedCrawledTrend.from_crawled_trend(e) for e in en]
