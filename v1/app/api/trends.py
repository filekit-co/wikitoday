import logging
import pprint
from typing import Any, Callable

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.logger import get_colored_logger
from consts import TargetCountryCode
from domain.entities import Language
from infra.github import push_folders
from infra.google_trends import daily_trends
from infra.gpt import regenerate_articles
from infra.markdown import to_folders
from infra.news_crawler import from_trends
from infra.sns import twitter
from infra.sns.base import post_sns
from infra.translate import translate_articles, translate_crawled_trends
from mocks import step5, step6

router = APIRouter(prefix='/trends', tags=["trends"])
logger = logging.getLogger(__name__)
colored = get_colored_logger(__name__)

async def aperform_step(step_number: int, func: Callable, *args, **kwargs) -> Any:
    colored.info(f"########## Step {step_number}: {func.__name__}")
    result = await func(*args, **kwargs)
    logger.info(f'step{step_number} = {pprint.pformat(result)}')
    return result

def perform_step(step_number: int, func: Callable, *args, **kwargs) -> Any:
    colored.info(f"########## Step {step_number}: {func.__name__}")
    result = func(*args, **kwargs)
    logger.info(f'step{step_number} = {pprint.pformat(result)}')
    return result


@router.get("/")
async def generate_news(country: TargetCountryCode, date: str | None = None):
    # date schema YYYYMMDD i.g 20230803
    google_trends = await aperform_step(1, daily_trends, country, date)
    crawled_trends = await aperform_step(2, from_trends, google_trends)
    translated_trends = await aperform_step(3, translate_crawled_trends, crawled_trends)
    regenerated_articles = await aperform_step(4, regenerate_articles, translated_trends)
    translated_articles = await aperform_step(5, translate_articles, country, regenerated_articles)
    folders = perform_step(6, to_folders, translated_articles, date)
    await push_folders(folders, country)

    today = folders[0].today
    for article in translated_articles:
        article.print_sns_articles(today)
    return JSONResponse(content=jsonable_encoder(folders))



    # us_twitter_pusher = twitter.get_pusher_by_language(language=Language.EN_US)
    # await post_sns(
    #     us_twitter_pusher,
    #     title='Al Nassr Advances To The Arab Club Champions Cup Final With A Thrilling Victory Over Al Shorta',
    #     lead='ollow for highlights from the Arab Club Champions Cup match between Al Shorta and Al Nassr, which ended with Al Nassr securing a spot in the final.',
    #     category='Sports',
    #     keywords='#AlNassr #AlShorta #ArabClubChampionsCup #Final #Victory #PrinceSultanBinAbdulAzizStadium #Abha #SaudiArabia #Alaqidi #Goalkeeper #LastDitchSave #Sportstar',
    #     url='https://wikitoday.io/EN-US/news/Sports/2023-08-10/Al-Nassr-advances-to',
    # )
    