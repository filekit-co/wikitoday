from pprint import pprint

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from consts import TargetCountryCode
from infra.github import push_folders
from infra.google_trends import daily_trends
from infra.gpt import regenerate_articles
from infra.markdown import to_folders
from infra.news_crawler import from_trends
from infra.translate import translate_articles, translate_crawled_trends
from utils import color_print

router = APIRouter(prefix='/trends', tags=["trends"])


@router.get("/")
async def generate_news(country: TargetCountryCode, date: str | None = None):
    # date schema YYYYMMDD i.g 20230803

    color_print("########## Step 1: Getting daily trends")
    google_trends = await daily_trends(country, date)
    print('step1 = ' + pprint.pformat(google_trends))

    color_print("########## Step 2: Crawling trends")
    crawled_trends = await from_trends(google_trends)
    print('step2 = ' + pprint.pformat(crawled_trends))

    color_print("########## Step 3: Translating crawled trends")
    translated_trends = await translate_crawled_trends(crawled_trends)
    print('step3 = ' + pprint.pformat(translated_trends))

    color_print("########## Step 4: Regenerating articles")
    regenerated_articles = await regenerate_articles(translated_trends)
    print('step4 = ' + pprint.pformat(regenerated_articles))

    color_print("########## Step 5: Translating articles")
    translated_articles = await translate_articles(regenerated_articles)
    print('step5 = ' + pprint.pformat(translated_articles))
    
    color_print("########## Step 6: Converting to folders")
    folders = to_folders(translated_articles, date)
    print('step6 = ' + pprint.pformat(folders))

    color_print("########## Step 7: Pushing folders")
    await push_folders(folders, country)

    return JSONResponse(content=jsonable_encoder(folders))