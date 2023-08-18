import logging
from abc import ABC, abstractmethod
from typing import List

from domain.entities import Article
from jinja2 import Template

logger = logging.getLogger(__name__)
_sns_template = """
title: '{{ title }}'
summary: '{{ lead }}'
category: '{{ category }}'
keywords: '{{ keywords }}'

{{ url }}
"""
SNS_TEMPLATE = Template(_sns_template)


class SNSMarketingPostPusher(ABC):

    @abstractmethod
    async def post_message(self, message: str, **kwargs):
        """
        SNS 플랫폼에 메시지를 게시합니다.
        :param message: 게시할 메시지 내용
        :param kwargs: 플랫폼별 추가 파라미터
        """
        pass


async def post_sns(pusher: SNSMarketingPostPusher, title:str, lead:str, category: str, keywords: str, url: str):
    message = SNS_TEMPLATE.render({
        'title': title,
        'lead': lead,
        'category': category,
        'keywords': keywords,
        'url': url,
    })
    logger.error(message)
    await pusher.post_message(message)
    


async def build(articles: List[Article]):
    ...