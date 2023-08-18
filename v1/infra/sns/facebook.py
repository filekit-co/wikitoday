import logging

from app.config import get_env
from infra.sns.base import SNSMarketingPostPusher

logger = logging.getLogger(__name__)
_env = get_env()

class FacebookPostPusher(SNSMarketingPostPusher):


    async def post_message(self, message: str, page_id: str):
        print(f"Facebook 페이지 {page_id}에 메시지 게시: {message}")


def get_pusher() -> FacebookPostPusher:
    return FacebookPostPusher(_env['FACEBOOK_API_KEY'])

