import logging

import httpx
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import InvalidCountryCodes
from consts import TARGET_COUNTRY_CODES
from infra.google_trends import daily_trends
from infra.news_crawler import NewsPlease
from infra.requests import get_client

router = APIRouter(prefix='/trends', tags=["trends"])


@router.get("/")
async def get_trends(country: str, client: httpx.AsyncClient = Depends(get_client)):
    # 0. cronjob per 나라 05:00 am 기준 (우리나라는 그 나라에 맞춰서)
    # 1. coutries
    # 2. news link unique
    # 3. check is_unique url
    # 4. url 저장 
    # cronjob-hook > countries > trends > articles > crawl > regenerate > translate > to_markdown > push github, sns

    if country not in TARGET_COUNTRY_CODES:
        raise InvalidCountryCodes

    trends = await daily_trends(client, country)
    urls = []
    for trend in trends:
        urls.extend(trend.hrefs)
    logging.error(urls)
    
    result = await NewsPlease.from_urls(urls, timeout=6)

    
    
    # TODO: db url unique check
    # articles = await crawl(trends)
    # markdown = gpt(articles)
    # translate()


    return JSONResponse(content=jsonable_encoder(result))