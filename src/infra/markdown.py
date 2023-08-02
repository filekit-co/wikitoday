from datetime import date
from typing import List

from jinja2 import Template

from domain.entities import Article, Folder, Markdown

_markdown_template = """---
title: {{ content.title }}
description: {{ content.lead }}
category: {{ category }}
keywords: {{ keywords }}
date: {{ date }}
author: wikitoday.io
language: {{ content.language }}
---

# Summary

<figure>
    <img src="{{ images[0].url }}" alt="{{ images[0].source }}" />
    <figcaption>
        <h4> from {{ images[0].source }}</h4>
    </figcaption>
</figure>

{{ content.lead }}

## QnA

{% for i, qna in qna %}
<details>
    <summary><b>{{ i }}. {{ qna.question }}</b></summary>
    {{ qna.answer }}
</details>
{% endfor %}

## {{ content.title }}

_{{ date }} - wikitoday_

{{ content.body1 }}

<figure>
    <img src="{{ images[1].url }}" alt="{{ images[1].source }}" />
    <figcaption>
        <h4> from {{ images[1].source }}</h4>
    </figcaption>
</figure>

{{ content.body2 }}

_end_

"""

ARTICLE_TEMPLATE = Template(_markdown_template)


def to_folders(articles: List[Article]) -> List[Folder]:
    today = date.today()
    folders = []
    for article in articles:
        markdowns = []
        for content in article.contents:
            markdown = Markdown(
                language = content.language,
                md = ARTICLE_TEMPLATE.render({
                    "category": article.category,
                    "keywords": article.keywords,
                    "content": content,
                    "date": today,
                    "images": article.images,
                    "qna": enumerate(content.qna_list)
                })
            )
            markdowns.append(markdown)
        folders.append(
            Folder(
                today = today,
                folder_name = article.url_safe_name,
                mds = markdowns
            )
        )
    return folders




