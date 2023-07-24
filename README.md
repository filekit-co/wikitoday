# `llm` server
> for making ai news using the LLM model


![arch](https://raw.githubusercontent.com/filekit-co/llm/main/docs/arch.iuml)


Below is the server architecture I envisioned for making ai news using the LLM model.

1. Cronjob
2. Data Source server
  2-1. Get ranked link from 3rd party list posts api (i.e google trends api, youtube realtime, hot tweets, hot facebook posts)
  2-2. Pass to crawler
  2-3. Crawl links
    - crawl images and text contents
  2-4. Pass it to `AI server`
1. AI server(Regenerate contents)
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
2. Translate `<article>.md` to other languages (5 ~ 10 languages)
3. Push it to news frontend github repository
4. CI/CD trigger
5. Build
6. Deploy with cloud flare pages

