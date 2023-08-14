import asyncio
import json
import logging
from typing import List

import httpx

from app.config import get_env
from consts import TargetCountryCode
from domain.entities import (Article, CrawledTrend, Language,
                             TranslatedCrawledTrend)
from domain.localization.cultural_mapping import \
    get_culturally_relevant_languages

logger = logging.getLogger(__name__)

_cfg = get_env()
DEEPL_API_KEY = _cfg["DEEPL_API_KEY"]
# FREE_DEEPL_URL = 'https://api-free.deepl.com/v2/translate'
PRO_DEEPL_URL = 'https://api.deepl.com/v2/translate'

async def translate_text(client: httpx.AsyncClient, texts: List[str], target_lang: Language = Language.EN_US) -> dict:
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
    
    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'text': texts,
        'target_lang': target_lang
    }
    try:
        response = await client.post(PRO_DEEPL_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error(f"given texts: {texts}")
        logger.error(f"Error message: {e.response.text}")
        return None
    
    translated = response.json()
    # .replace('"', "'") to avoid gpt invalid json string
    return [t['text'].replace('"', "'") for t in translated['translations']]


async def translate_crawled_trends(trends: List[CrawledTrend], target_lang: Language = Language.EN_US) -> List[TranslatedCrawledTrend]:
    en = [t for t in trends if t.is_en]
    others = [t for t in trends if not t.is_en]

    async with httpx.AsyncClient() as client:
        tasks = [(i, translate_text(client, other.articles, target_lang)) for i, other in enumerate(others)]
        tasks = {i: task for i, task in tasks}
        responses = {
            i: await task for i, task in tasks.items()
        }        
        return [
            TranslatedCrawledTrend.from_crawled_trend(
                others[idx], 
                response
            )
            for idx, response in responses.items()
            if response 
        ] + [TranslatedCrawledTrend.from_crawled_trend(e) for e in en]


# en -> multiple languages
async def translate_articles(news_origin_country_code: TargetCountryCode, articles: List[Article]):
    # key format = (article index, target_lang_code)
    async with httpx.AsyncClient() as client:
        tasks = [
            ((i, target_lang), translate_text(client, article.to_list(), target_lang)) 
            for i, article in enumerate(articles)
            for target_lang in get_culturally_relevant_languages(news_origin_country_code, include_english=False)
        ]
        tasks = {key: task for key, task in tasks}
        responses = await asyncio.gather(
            *(task for task in tasks.values()), 
            return_exceptions=True
        )

    for (i, target_lang), response in zip(tasks.keys(), responses):
        if response is None: 
            continue
        
        try:
            articles[i].append_translation(response, target_lang)
        except Exception as e:
            logger.error(f"Error during appending translation: {e}, Params: {(i, target_lang)}")
        
    return articles