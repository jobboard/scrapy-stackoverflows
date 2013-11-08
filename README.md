# Stackoverflow Career (Job & Companies) scrapper

Quick n Dirty implementation with scrappy to scrap all jobs and companies on http://careers.stackoverflow.com/jobs

# How to run
```bash
➜  scrapy-stackoverflows git:(master) ✗ scrapy list
stackoverflowjob
stackoverflowcompany
```

```bash
➜  scrapy-stackoverflows git:(master) ✗ scrapy crawl stackoverflowjob -o test.json -t json
```

You can also deploy scrapy as a daemon, see #http://scrapyd.readthedocs.org/en/latest/

# Sample output
https://github.com/jayzeng/scrapy-stackoverflows/blob/master/jobs.json

# TODO
- Cache with Redis
- Backoff and retry base upon (e.g: http status code)
- Store into db storage (e.g: Mongo, Mysql or postgresql)
- A thin web interface to manipulate jobs (schedule, cancel jobs etc)
- Add more spiders and crawlers to cover other job boards
- Deploy it as a real-time API that returns job JSON
- Basic machine learning with PredictionIO or Mahout
- Ability to answer basic questions like, what is the top 10 hot jobs in Seattle?
