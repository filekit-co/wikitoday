import logging

import httpx
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import InvalidCountryCodes
from consts import TARGET_COUNTRY_CODES
from infra.google_trends import daily_trends
from infra.gpt import regenerate
from infra.markdown import to_folders
from infra.news_crawler import from_trends
from infra.translate import translate_articles, translate_crawled_trends
from mocks import step_5

router = APIRouter(prefix='/trends', tags=["trends"])




@router.get("/")
async def generate_news(country: str):
    # 0. cronjob per 나라 05:00 am 기준 (우리나라는 그 나라에 맞춰서)
    # 1. coutries
    # 2. news link unique
    # 3. check is_unique url
    # 4. url 저장 
    # cronjob-hook > countries > trends > articles > crawl > regenerate > translate > to_markdown > push github, sns
    
    if country not in TARGET_COUNTRY_CODES:
        raise InvalidCountryCodes()

    # google_trends = await daily_trends(country)
    # crawled_trends = await from_trends(google_trends)
    # translated_trends = await translate_crawled_trends(crawled_trends)
    
    # regenerated_articles = await regenerate(translated_trends)
    # translated_articles = await translate_regenerated_articles(regenerated_articles)

    # markdown_articles = await to_markdown(translated_articles)
    folders = to_folders(step_5)
    
    # await push(markdowned_articles)
    return JSONResponse(content=jsonable_encoder(folders))
