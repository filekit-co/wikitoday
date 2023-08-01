# `wikitoday.io` server
> for making ai news using the LLM model


<p align="center">
<img src="https://github.com/filekit-co/wikitoday/assets/37536298/7bdab99e-f7e7-400d-878a-eb56d044e024" width=900 />
<br/>
<br/>
<img src="http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/filekit-co/llm/main/docs/v1.iuml" />
</p>






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
> pyenv local 3.11
> poetry env use $(pyenv which python)
> poetry env info
> poetry add scrapy fastapi 'uvicorn[standard]' httpx
```

- [m1 clang with lxml error](https://github.com/lxml/lxml/pull/360)

## arch
- [mongo](https://chat.openai.com/c/ceecbe13-bf65-4dab-96df-42b66a87fc08)
  - [atlas](https://cloud.mongodb.com/v2/64bf6da368f1a3195493f775#/clusters/starterTemplates)
- [google trends](https://github.com/deedy5/google_trends)
- [crawl and parse text](https://chat.openai.com/c/849ac652-e1cd-4672-ba6e-f2468ce5c9d7)
- llm server
  - crawler
  - parse text
  - regenerator
