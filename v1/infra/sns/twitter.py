import logging

from tweepy.asynchronous.client import AsyncClient

from app.config import get_env
from domain.entities import Language
from infra.sns.base import SNSMarketingPostPusher

logger = logging.getLogger(__name__)
_env = get_env()

class TwitterPostPusher(SNSMarketingPostPusher):
    _client = None

    def __init__(self, bearer_token):
        self._client = AsyncClient(
            bearer_token=bearer_token,
        )


    async def post_message(self, message: str):
        try:
            response = await self._client.create_tweet(
                text=message,
                user_auth=False # to use OAUTH2.0 with bearer_token
            )
            
        except Exception as e:
            logger.error(response)
            logger.exception(e)
            



US_TWITTER_PUSHER = TwitterPostPusher(
    bearer_token=_env['US_TWITTER_BEARER_TOKEN'],
)



ASIA_TWITTER_PUSHER = TwitterPostPusher(
    bearer_token=_env['ASIA_TWITTER_BEARER_TOKEN'],

)
EUR_TWITTER_PUSHER = TwitterPostPusher(
    bearer_token=_env['EUR_TWITTER_BEARER_TOKEN'],
)


# 언어를 대륙별 Twitter Pusher와 매핑
continent_pusher_mapping = {
    'US': {Language.EN_US, Language.ES, Language.PT_BR}, # 미국 대륙 언어
    'ASIA': {Language.ZH, Language.JA, Language.KO, Language.ID, Language.KO}, # 아시아 대륙 언어
    'EUR': {Language.BG, Language.CS, Language.DA, Language.DE, Language.EL, Language.EN_GB, Language.ET, Language.FI, Language.FR, Language.HU, Language.IT, Language.LT, Language.LV, Language.NB, Language.NL, Language.PL, Language.PT_PT, Language.RO, Language.RU, Language.SK, Language.SL, Language.SV, Language.TR, Language.UK}, # 유럽 대륙 언어
}

pusher_by_continent = {
    'US': US_TWITTER_PUSHER,
    'ASIA': ASIA_TWITTER_PUSHER,
    'EUR': EUR_TWITTER_PUSHER,
}

# 언어에 따른 Twitter Pusher 반환 함수
def get_pusher_by_language(language: Language):
    for continent, languages in continent_pusher_mapping.items():
        if language in languages:
            return pusher_by_continent[continent]
    return US_TWITTER_PUSHER # 기본값

