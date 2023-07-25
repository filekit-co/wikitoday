# `wikitoday.io` server
> for making ai news using the LLM model

![arch](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/filekit-co/llm/main/docs/v1.iuml)


Below is the server architecture I envisioned for making ai news using the LLM model.

1. Cronjob
2. Data Source server
  1. Get ranked link from 3rd party list posts api (i.e google trends api, youtube realtime, hot tweets, hot facebook posts)
  2. Pass to crawler
  3. Crawl links
    - crawl images and text contents
  2-4. Pass it to `AI server`
3. AI server(Regenerate contents)
  1. pass crawled data to `llm`( i.e gpt4-api or bard api) with prompt
  2. prompt details
    1. seo (english)
      1. title
      2. description
      3. keywords
      4. canonical path name
    2. contents (english)
      1. summary in line
      2. 6~8 group of Q&A 
      3. regenerated article
  3. Save contents as a `<article>.md`
4. Translate `<article>.md` to other languages (5 ~ 10 languages)
5. Push it to news frontend github repository
6. CI/CD trigger
7. Build
8. Deploy with cloud flare pages

## init

```sh
> poetry init
> pyenv local 3.10
> python -V
Python 3.9.16
> poetry env use $(pyenv which python)
Creating virtualenv llm-UTZ1ts9j-py3.9 in /Users/minwook/Library/Caches/pypoetry/virtualenvs
Using virtualenv: /Users/minwook/Library/Caches/pypoetry/virtualenvs/llm-UTZ1ts9j-py3.9
> poetry env info

Virtualenv
Python:         3.9.16
System
Platform:   darwin
OS:         posix
Python:     3.9.16
```

