import asyncio
import json
import logging
from typing import List

import httpx

from app.config import get_env
from app.exceptions import TranslationError
from domain.entities import (Article, CrawledTrend, Language,
                             TranslatedCrawledTrend)

_cfg = get_env()
DEEPL_API_KEY = _cfg["DEEPL_API_KEY"]

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
    url = 'https://api-free.deepl.com/v2/translate'
    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'text': texts,
        'target_lang': target_lang
    }
    try:
        response = await client.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        logging.error(f"An error occurred: {e}")
        logging.error(f"given texts: {texts}")
        logging.error(f"Error message: {e.response.text}")
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
async def translate_articles(articles: List[Article]):
    # key format = (article index, target_lang_code)
    async with httpx.AsyncClient() as client:
        tasks = [
            ((i, target_lang), translate_text(client, article.to_list(), target_lang)) 
            for i, article in enumerate(articles)
            for target_lang in Language.target_languages()
        ]
        # Unpack the article and its associated translation task
        tasks = {key: task for key, task in tasks}
        # Gather the results, keeping track of which article each one is associated with
        responses = {
            key: await task for key, task in tasks.items()
        }
    
    for (i, target_lang), response in responses.items():
        articles[i].append_translation(response, target_lang)
    
    return articles