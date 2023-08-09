import asyncio
import json
import logging
from typing import List

import openai
from jinja2 import Template

from app.config import get_env
from consts import GPT_MODEL
from domain.entities import TranslatedCrawledTrend
from src.domain.entities import Article

logger = logging.getLogger(__name__)
_env = get_env()
OPENAI_API_KEY = _env["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY


SYS_PROMPT = "You are an AI journalist for \'Wikitoday\', an automated news service.\nYour task is to generate engaging and SEO-friendly news articles based on given \'KEYWORD\' and related \'ARTICLES\'. \nYour article should be written in a style that is indistinguishable from human journalists without any reference to the journalist name or news provider that wrote the original article. \nThe ultimate goal of \'Wikitoday\' is to convey information to busy readers as efficiently as possible and to attract a large audience for effective advertising revenue.\n"
FUNCTION_NAME = "generate_news_article"
FUNCTIONS = [
    {
        "name": FUNCTION_NAME,
        "description": "Generate an news article by referring to the given articles of the keyword. !IMPORTANT: you must response with json format below",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "An article title, to get as many people interested in your article as possible shortly"
                },
                "lead": {
                    "type": "string",
                    "description": "An article lead, concisely state the facts of the most important article, and write the most important content of the entire article in 1-2 sentences"
                },
                "body": {
                    "type": "string",
                    "description": "An article body, without any reference to the journalist name or news provider that wrote the original article"
                },
                "qna": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "question": {
                                "type": "string"
                            },
                            "answer": {
                                "type": "string"
                            }
                        },
                        "required": ["question", "answer"]
                    },
                    "description": "An array of Question and Answer, write 3 to 7 Q&As about what people might be curious in this article"
                },
                "category": {
                    "type": "string",
                    "enum": ["Politics", "International", "Economy", "Technology", "Science", "Health", "Entertainment", "Sports", "Nature", "Education", "Lifestyle", "Opinion", "Crime"],
                    "description": "An article enum typed category"
                },
            },
            "required": ["title", "lead", "body", "qna", "category"]
        }
    }
]
_str_user_template = """Below are {{ num_articles }} articles written with the keyword {{ keyword }}. Please give me the json response according to WIKITODAY's requirements.


```
{{ articles }}
```


!IMPORTANT Answer in English Never break character:
"""
USER_PROMPT_TEMPLATE = Template(_str_user_template)

# TODO: if category not included change it to fallback category.
def _generate_template_articles(keyword, articles):
    separator = "\n---\n"
    articles_text = separator.join(articles)
    
    return USER_PROMPT_TEMPLATE.render({
        "keyword": keyword,
        "num_articles": len(articles),
        "articles": articles_text
    })

async def _regenerate(trend: TranslatedCrawledTrend):
    response = None
    try:
        response = await openai.ChatCompletion.acreate(
                    model=GPT_MODEL,
                    messages=[
                        {
                        "role": "system",
                        "content": SYS_PROMPT
                        },
                        {
                        "role": "user",
                        "content": _generate_template_articles(trend.str_keywords, trend.articles)
                        },
                    ],
                    functions=FUNCTIONS,
                    function_call={"name": FUNCTION_NAME},
                    temperature=1,
                    max_tokens=10000,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
        )
        function_call = response.choices[0].message.function_call
        article = json.loads(function_call.arguments)
        return Article.from_dto(trend, article)
    except Exception as e:
        if response:
            logger.error(response)        
        logger.error(f"An error occurred while generating article for trend\n\n {trend} \n\n{e}")
        return None


async def regenerate_articles(trends: List[TranslatedCrawledTrend]) -> List[Article]:
    tasks = [_regenerate(trend) for trend in trends]
    responses = await asyncio.gather(*tasks)
    # Filter out None results
    articles = [article for article in responses if article is not None]
    return articles
