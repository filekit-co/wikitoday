# `llm` server
> for making ai news using the LLM model

![llm](//www.plantuml.com/plantuml/png/NP7DRjim48JlV8ffxbPHfp-5K0H9x2BmhQWBzBmMDp8RYXIMgnXz-vACwaG6U21tlkN-p6rI4fq6RzxfaGU6iBN2AQsywu-QNsRCWElSI46naHZ-nCCYThKb9UpZ91qZiJopN84IjllzahlRlPNlTXVoBw6GFAcBeGBrlKGUd1wd0txo60jIBqjYu-DayUX962Frd2ftFpblb-3lx_SlNVBeurzZvicmkYcDjrYlFZHuO8LGU68BxyAJoSeRODtW1wK4ZUY4Jfxb0hXki2b2JKwpM0OluiSvssdvuBmROx9-ngvB5sF6vWeMbfHAWlV31RdEfCHXL5XMSZujzTBDdfuPNGpAGHCe7tohI_5yqmpsNBkklaLkyRyfl0Hhk935WHQVyYnJEiwp13ubF4ejOz6_U2OPJ4wZv5sNfDVaptbBk_URBSxnQbUBBmrKND-pb5yFrSCgPMRshSNNPhxYb0kXk_JVt7Amq-3_0G00)

Below is the server architecture I envisioned for making ai news using the LLM model.

1. Cronjob
2. Data Source server
  2-1. Get ranked link from 3rd party list posts api (i.e google trends api, youtube realtime, hot tweets, hot facebook posts)
  2-2. Pass to crawler
  2-3. Crawl links
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

