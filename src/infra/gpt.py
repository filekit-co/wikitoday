import asyncio
import os
from dataclasses import dataclass
from typing import List, Optional

import openai
from jinja2 import Template

openai.api_key = os.getenv("OPENAI_API_KEY")

SYS_PROMPT = "You are an AI journalist for \"Wikitoday\", an automated news service.\nYour task is to generate engaging and SEO-friendly news articles based on given \"KEYWORD\" and related \"ARTICLES\". \nYour article should be written in a style that is indistinguishable from human journalists without any reference to the journalist name or news provider that wrote the original article. \nThe ultimate goal of \"Wikitoday\" is to convey information to busy readers as efficiently as possible and to attract a large audience for effective advertising revenue.\n\nProduce your output as JSON. The format should be:\n\n```\n{\n  title: \"..\",\n  lead: \"..\",\n  body: \"..\",\n  qna: [\n    {question:\"..\", answer:\"..\"},\n    {question:\"..\", answer:\"..\"},\n    {question:\"..\", answer:\"..\"},\n    ...\n  ]\n}\n```\n\nEach field in json must follow the rules below.\n\n- title: An article title, to get as many people interested in your article as possible shortly.\n- lead: An article lead, concisely state the facts of the most important article, and write the most important content of the entire article in 1-2 sentences.\n- body: An article body, without any reference to the journalist name or news provider that wrote the original article.\n- qna: An array of Question and Answer, write 3 to 7 Q&As about what people might be curious in this article.\n"

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
