import asyncio
import os
from dataclasses import dataclass
from typing import List, Optional

import openai
import tiktoken
from jinja2 import Template

from app.config import get_env
from consts import GPT_MODEL

_cfg = get_env()
OPENAI_API_KEY = _cfg["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

_str_user_template = """
Below are {{ num_articles }} articles written with the keyword {{ keyword }}. Please answer them according to WIKITODAY requirements.

```
{{ articles }}
```

!IMPORTANT Answer in English Never break character:
"""
USER_PROMPT_TEMPLATE = Template(_str_user_template)


@dataclass
class QnA:
    question: str
    answer: str

@dataclass
class Article:
    title: Optional[str] = None
    lead: Optional[str] = None
    body: Optional[str] = None
    qna: Optional[List[QnA]] = None
    
    
    @property
    def to_markdown(self):
        # TODO: check how to convert it to a markdown format
        ...



def _generate_template_articles(keyword, articles):
    separator = "\n---\n"
    articles_text = separator.join(articles)
    
    return USER_PROMPT_TEMPLATE.render({
        "keyword": keyword,
        "num_articles": len(articles),
        "articles": articles_text
    })


async def regenerate(trends):
    model = "gpt-3.5-turbo-16k-0613"

    # TODO: parse to markdown

    articles = await asyncio.gather(*[
        Article(
        openai.ChatCompletion.acreate(
            model=model,
            messages=[
                {
                "role": "system",
                "content": SYS_PROMPT
                },
                {
                "role": "user",
                "content": _generate_template_articles(t.keyword, t.articles)
                },
            ],
            temperature=0.7,
            max_tokens=10000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        )
        for t in trends
    ])
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