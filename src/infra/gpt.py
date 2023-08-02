import asyncio
import json
import os
from dataclasses import dataclass, field
from typing import List, Optional

import openai
import tiktoken
from jinja2 import Template

from app.config import get_env
from app.exceptions import GptInvalidLengthError
from consts import GPT_MODEL
from domain.entities import TranslatedCrawledTrend
from src.domain.entities import Article

_cfg = get_env()
OPENAI_API_KEY = _cfg["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY


# SYS_PROMPT = "You are an AI journalist for \'Wikitoday\', an automated news service.\nYour task is to generate engaging and SEO-friendly news articles based on given \'KEYWORD\' and related \'ARTICLES\'. \nYour article should be written in a style that is indistinguishable from human journalists without any reference to the journalist name or news provider that wrote the original article. \nThe ultimate goal of \'Wikitoday\' is to convey information to busy readers as efficiently as possible and to attract a large audience for effective advertising revenue.\n\nProduce your output as JSON. The format should be:\n\n```\n{\n  title: \'..\',\n  lead: \'..\',\n  body: \'..\',\n  qna: [\n    {question:\'..\', answer:\'..\'},\n    {question:\'..\', answer:\'..\'},\n    {question:\'..\', answer:\'..\'},\n    ...\n  ]\n}\n```\n\nEach field in json must follow the rules below.\n\n- title: An article title, to get as many people interested in your article as possible shortly.\n- lead: An article lead, concisely state the facts of the most important article, and write the most important content of the entire article in 1-2 sentences.\n- body: An article body, without any reference to the journalist name or news provider that wrote the original article.\n- qna: An array of Question and Answer, write 3 to 7 Q&As about what people might be curious in this article."
SYS_PROMPT = "You are an AI journalist for \'Wikitoday\', an automated news service.\nYour task is to generate engaging and SEO-friendly news articles based on given \'KEYWORD\' and related \'ARTICLES\'. \nYour article should be written in a style that is indistinguishable from human journalists without any reference to the journalist name or news provider that wrote the original article. \nThe ultimate goal of \'Wikitoday\' is to convey information to busy readers as efficiently as possible and to attract a large audience for effective advertising revenue.\n"
# FUNCTIONS = [
#     {
#         "name": "generate_news_article",
#         "description": "Generate an news article by referring to the given articles of the keyword. !IMPORTANT: you must response with json format below",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "keyword": {
#                     "type": "string",
#                     "description": "The main keyword related to the article",
#                 },
#                 "articles": {
#                     "type": "array",
#                     "items": {
#                         "type": "string",
#                     },
#                     "description": "The list of related articles based on the keyword"
#                 },
#             },
#             "required": ["keyword", "articles"]
#         },
#         "return": {
#             "type": "object",
#             "properties": {
#                 "title": {
#                     "type": "string",
#                     "description": "An article title, to get as many people interested in your article as possible shortly"
#                 },
#                 "lead": {
#                     "type": "string",
#                     "description": "An article lead, concisely state the facts of the most important article, and write the most important content of the entire article in 1-2 sentences"
#                 },
#                 "body": {
#                     "type": "string",
#                     "description": "An article body, without any reference to the journalist name or news provider that wrote the original article"
#                 },
#                 "qna": {
#                     "type": "array",
#                     "items": {
#                         "type": "object",
#                         "properties": {
#                             "question": {
#                                 "type": "string"
#                             },
#                             "answer": {
#                                 "type": "string"
#                             }
#                         },
#                         "required": ["question", "answer"]
#                     },
#                     "description": "An array of Question and Answer, write 3 to 7 Q&As about what people might be curious in this article"
#                 },
#                 "category": {
#                     "type": "string",
#                     "enum": ["Politics", "World/International", "Business/Economy", "Technology", "Science", "Health", "Entertainment", "Sports", "Environment/Nature", "Education", "Lifestyle", "Opinion/Editorial"],
#                     "description": "An article enum typed category"
#                 },
#             },
#             "required": ["title", "lead", "body", "qna", "category"]
#         }
#     }
# ]
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
                    "enum": ["Politics", "World/International", "Business/Economy", "Technology", "Science", "Health", "Entertainment", "Sports", "Environment/Nature", "Education", "Lifestyle", "Opinion/Editorial"],
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





def _generate_template_articles(keyword, articles):
    separator = "\n---\n"
    articles_text = separator.join(articles)
    
    return USER_PROMPT_TEMPLATE.render({
        "keyword": keyword,
        "num_articles": len(articles),
        "articles": articles_text
    })



async def regenerate(trends: List[TranslatedCrawledTrend]) -> List[Article]:
    responses = await asyncio.gather(*[
        openai.ChatCompletion.acreate(
            model=GPT_MODEL,
            messages=[
                {
                "role": "system",
                "content": SYS_PROMPT
                },
                {
                "role": "user",
                "content": _generate_template_articles(t.str_keywords, t.articles)
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
        for t in trends
    ])

    if len(trends) != len(responses):
        raise GptInvalidLengthError()

    result = []
    for trend, response in zip(trends, responses):
        # https://github.com/openai/openai-cookbook/blob/3115683f14b3ed9570df01d721a2b01be6b0b066/examples/azure/functions.ipynb#L255
        function_call = response.choices[0].message.function_call
        article = json.loads(function_call.arguments)
        result.append(
            Article.from_dto(trend, article)
        )
    
    return result
    
    

# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_messages(messages, model=GPT_MODEL):
    """Return the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens