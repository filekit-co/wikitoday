import logging

import httpx
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import InvalidCountryCodes
from consts import TARGET_COUNTRY_CODES
from infra.google_trends import daily_trends
from infra.gpt import regenerate
from infra.news_crawler import from_trends
from infra.requests import get_client

router = APIRouter(prefix='/trends', tags=["trends"])


from domain.entities import GoogleTrend, TrendArticleMeta

mocked_google_trends = [GoogleTrend(query='태풍',
             related_quries=['태풍경로', '태풍 카눈', '카눈'],
             articles=[TrendArticleMeta(url='https://imnews.imbc.com/news/2023/society/article/6509804_36126.html',
                                        source='MBC뉴스'),
                       TrendArticleMeta(url='https://www.voakorea.com/a/7205712.html',
                                        source='VOA Korea')]),
 GoogleTrend(query='김은경',
             related_quries=['김은경 혁신위원장'],
             articles=[TrendArticleMeta(url='https://imnews.imbc.com/replay/2023/nwtoday/article/6509639_36207.html',
                                        source='MBC뉴스'),
                       TrendArticleMeta(url='https://www.newspim.com/news/view/20230801000812',
                                        source='뉴스핌')]),
 GoogleTrend(query='콘크리트 유토피아',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://news.kbs.co.kr/news/view.do?ncd=7737058',
                                        source='KBS뉴스'),
                       TrendArticleMeta(url='http://m.cine21.com/news/view/?mag_id=103244',
                                        source='씨네21')]),
 GoogleTrend(query='잼버리',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.jjan.kr/article/20230801580159',
                                        source='전북일보'),
                       TrendArticleMeta(url='https://www.jjan.kr/article/20230801580194',
                                        source='전북일보')]),
 GoogleTrend(query='뉴스 속보',
             related_quries=[],
             articles=[TrendArticleMeta(url='http://www.jejusori.net/news/articleView.html?idxno=417699',
                                        source='제주의소리')]),
 GoogleTrend(query='주호민 논란',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://news.mt.co.kr/mtview.php?no=2023080109490517865',
                                        source='머니투데이'),
                       TrendArticleMeta(url='https://www.chosun.com/entertainments/enter_general/2023/07/31/7SJ3H67ZND2FYM3IVFHLPN3UCE/',
                                        source='조선일보')]),
 GoogleTrend(query='소용없어 거짓말',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.mk.co.kr/star/broadcasting-service/view/2023/08/586940/',
                                        source='매일경제'),
                       TrendArticleMeta(url='http://www.monthlypeople.com/news/articleView.html?idxno=617868',
                                        source='월간인물')])]

@router.get("/")
async def generate_news(country: str, client: httpx.AsyncClient = Depends(get_client)):
    # 0. cronjob per 나라 05:00 am 기준 (우리나라는 그 나라에 맞춰서)
    # 1. coutries
    # 2. news link unique
    # 3. check is_unique url
    # 4. url 저장 
    # cronjob-hook > countries > trends > articles > crawl > regenerate > translate > to_markdown > push github, sns

    if country not in TARGET_COUNTRY_CODES:
        raise InvalidCountryCodes

    # google_trends = await daily_trends(client, country)
    
    crawled_trends = await from_trends(mocked_google_trends)
    # crawled_trends = await from_trends(google_trends)
    regenerated_articles = await regenerate(crawled_trends)
    # translated_articles = await translate(regenerated_articles)
    # markdowned_articles = await to_markdown(translated_articles)
    # await push(markdowned_articles)
    return JSONResponse(content=jsonable_encoder(regenerated_articles))