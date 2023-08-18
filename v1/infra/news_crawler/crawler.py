import asyncio
import logging

import httpx
import scrapy

from infra.news_crawler.decoder import decode_response

MAX_FILE_SIZE = 20000000
MIN_FILE_SIZE = 10
logger = logging.getLogger(__name__)

# customize headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}

class NewscrawlerItem(scrapy.Item):
    # ID of the article in the DB
    db_id = scrapy.Field()
    # Path of the file on the local filesystem
    local_path = scrapy.Field()
    # Filename
    filename = scrapy.Field()
    # absolute path of the file on the local filesystem
    abs_local_path = scrapy.Field()
    # When the article was last modified in the DB
    modified_date = scrapy.Field()
    # When the article was downloaded in the DB
    download_date = scrapy.Field()
    # Root domain from which the article came
    source_domain = scrapy.Field()
    url = scrapy.Field()
    # Title of the article
    html_title = scrapy.Field()
    # Response object from crawler
    spider_response = scrapy.Field()
    # Title of the article as store in the RSS feed
    rss_title = scrapy.Field()
    # Extracted article title
    article_title = scrapy.Field()
    # Extracted article description
    article_description = scrapy.Field()
    # Extracted article text body
    article_text = scrapy.Field()
    # Extracted top image of the article
    article_image = scrapy.Field()
    # Extracted article author
    article_author = scrapy.Field()
    # Extracted publishing date
    article_publish_date = scrapy.Field()
    # Extracted language of the article
    article_language = scrapy.Field()    


class SimpleCrawler:

    @staticmethod
    async def fetch_url(url, timeout=None):
        html_str = None
        try:
            async with httpx.AsyncClient(timeout=timeout, verify=False, headers=HEADERS) as client:
                response = await client.get(url, follow_redirects=True)
                response.raise_for_status()
        except (httpx.InvalidURL, httpx.RequestError):
            logger.error('malformed URL: %s', url)
        except httpx.HTTPStatusError as e:
            logger.error(e)
        else:
            # safety checks
            if response.text is None or len(response.text) < MIN_FILE_SIZE:
                logger.error('too small/incorrect: %s %s', url, len(response.text))
            elif len(response.text) > MAX_FILE_SIZE:
                logger.error('too large: %s %s', url, len(response.text))
            # if response.status_code not in (200, 302):
                # TODO: handle redirect
            else:
                html_str = decode_response(response)
        return (url, html_str)

    @staticmethod
    async def fetch_urls(urls, timeout=None):
        tasks = [SimpleCrawler.fetch_url(url, timeout=timeout) for url in urls]
        responses = await asyncio.gather(*tasks)
        return {k:v for (k, v) in responses}
