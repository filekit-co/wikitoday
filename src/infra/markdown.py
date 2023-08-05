import logging
from datetime import date, datetime
from typing import List, Optional

from domain.entities import Article, Folder, Markdown
from jinja2 import Template
from jinja2.exceptions import TemplateError

logger = logging.getLogger(__name__)

_markdown_template = """---
title: '{{ content.title }}'
description: '{{ content.lead }}'
category: '{{ category }}'
keywords: '{{ keywords }}'
date: '{{ date }}'
author: 'wikitoday.io'
language: '{{ content.language }}'
---

## Summary


{% if images|length > 0 %}
<figure>
    <img src="{{ images[0].url | e }}" alt="{{ images[0].source | e }}" />
    <figcaption>
        <h4> from {{ images[0].source | e }}</h4>
    </figcaption>
</figure>
{% endif %}

{{ content.lead }}

{% if qna %}
## QnA

{% for i, qna in qna %}
<details>
    <summary><b>{{ i }}. {{ qna.question | e }}</b></summary>
    {{ qna.answer | e }}
</details>
{% endfor %}
{% endif %}

## {{ content.title }}

_{{ date }} - wikitoday_

{{ content.body1 }}

{% if images|length > 1 %}
<figure>
    <img src="{{ images[1].url | e }}" alt="{{ images[1].source | e }}" />
    <figcaption>
        <h4> from {{ images[1].source | e }}</h4>
    </figcaption>
</figure>
{% endif %}

{{ content.body2 }}

"""

ARTICLE_TEMPLATE = Template(_markdown_template)

def _parse_date(date_string: date):
    """
    YYYYMMDD -> YYYY-MM-DD
    """
    return datetime.strptime(date_string, "%Y%m%d").date()


def to_folders(articles: List[Article], article_date: Optional[date] = None) -> List[Folder]:
    article_date = _parse_date(article_date) if article_date else date.today()

    folders = []
    for article in articles:
        markdowns = []
        for content in article.contents:
            try:
                markdown = Markdown(
                    language = content.language,
                    md = ARTICLE_TEMPLATE.render({
                        "category": article.category,
                        "keywords": article.keywords,
                        "images": article.images,
                        "content": content,
                        "date": article_date,
                        "qna": enumerate(content.qna_list)
                    })
                )
                markdowns.append(markdown)
            except TemplateError as e:
                logger.error(e)
                logger.error(content)

        folders.append(
            Folder(
                today = article_date,
                folder_name = article.url_safe_name,
                mds = markdowns
            )
        )
    return folders
