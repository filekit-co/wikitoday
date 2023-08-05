import logging
import pprint
from typing import Any, Callable

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.logger import get_colored_logger
from consts import TargetCountryCode
from infra.github import push_folders
from infra.google_trends import daily_trends
from infra.gpt import regenerate_articles
from infra.markdown import to_folders
from infra.news_crawler import from_trends
from infra.translate import translate_articles, translate_crawled_trends

router = APIRouter(prefix='/trends', tags=["trends"])
logger = logging.getLogger(__name__)
colored = get_colored_logger(__name__)

async def perform_step(step_number: int, func: Callable, *args, **kwargs) -> Any:
    colored.info(f"########## Step {step_number}: {func.__name__}")
    result = await func(*args, **kwargs)
    logger.info(f'step{step_number} = {pprint.pformat(result)}')
    return result



@router.get("/")
async def generate_news(country: TargetCountryCode, date: str | None = None):
    # date schema YYYYMMDD i.g 20230803
    google_trends = await perform_step(1, daily_trends, country, date)
    crawled_trends = await perform_step(2, from_trends, google_trends)
    translated_trends = await perform_step(3, translate_crawled_trends, crawled_trends)
    regenerated_articles = await perform_step(4, regenerate_articles, translated_trends)
    translated_articles = await perform_step(5, translate_articles, regenerated_articles)
    folders = await perform_step(6, to_folders, translated_articles, date)
    await perform_step(7, push_folders, folders, country)

    return JSONResponse(content=jsonable_encoder(folders))