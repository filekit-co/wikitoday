import logging
from datetime import date, datetime
from typing import List, Optional

from jinja2 import Template
from jinja2.exceptions import TemplateError

from domain.entities import Article, Folder, Markdown

logger = logging.getLogger(__name__)

_markdown_template = """---
title: '{{ content.title }}'
description: '{{ content.lead }}'
category: '{{ category }}'
keywords: '{{ keywords }}'
date: '{{ date }}'
author: 'wikitoday.io'
language: '{{ content.language }}'
candidLanguages: [{{ candid_languages|join(", ") }}]
{% if images|length > 0 %}thumbnail: '{{ images[0].url | e }}'{% endif %}
---

# {{ content.title }}

<p class="datetime"><em>{{ date|e }} - wikitoday<em></p>

<blockquote class="quote-container dark">
  <p class="quote-text dark">
    {{ content.lead|e }}
  </p>
</blockquote>

{% if images|length > 0 %}
<figure class=image-container>
    <img src="{{ images[0].url | e }}" alt="{{ images[0].source | e }}" />
    <figcaption>
        <h4> from {{ images[0].source | e }}</h4>
    </figcaption>
</figure>
{% endif %}

<hr class="article-hr" />

{% if qna %}
<div class="faq">
{% for i, qna in qna %}
<details class="group" {% if i == 0 %}open{% endif %}>
  <summary class="summary">
    <h2><b>Q. {{ qna.question | e }}</b></h2>
    <span class="icon-container">
      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-closed" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-open" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    </span>    
  </summary>
  <p>{{ qna.answer | e }}</p>
</details>
{% endfor %}
</div>
{% endif %}

<hr class="article-hr" />

<div class="article-body">
{{ content.body1 |e }}
</div>

{% if images|length > 1 %}
<figure class=image-container>
    <img src="{{ images[1].url | e }}" alt="{{ images[1].source | e }}" />
    <figcaption>
        <h4> from {{ images[1].source | e }}</h4>
    </figcaption>
</figure>
{% endif %}

<div class="article-body">
{{ content.body2 |e }}
</div>
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
        candid_languages = [f"'{lang}'" for lang in list(set([c.language for c in article.contents])) ]
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
                        "qna": enumerate(content.qna_list),
                        "candid_languages": candid_languages
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
