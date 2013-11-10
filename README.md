# Stackoverflow Career (Job & Companies) scrapper

Quick n Dirty implementation with scrappy to scrap all jobs and companies on http://careers.stackoverflow.com/jobs

# Dependencies
- scrappy (https://github.com/scrapy/scrapy)
- scrappy-redis (https://github.com/darkrho/scrapy-redis/)

# How to run
```bash
➜  scrapy-stackoverflows git:(master) ✗ scrapy list
stackoverflowjob
stackoverflowcompany
```

Import company schema into MySQL:
```
mysql -u user -p'pass' -H host jobs < company.sql
```

```bash
➜  scrapy-stackoverflows git:(master) ✗ scrapy crawl stackoverflowjob -o test.json -t json
```

Crawled results are cached in Redis:
```
redis 127.0.0.1:6379> LRANGE 'stackoverflowcompany:items' 0 11
```

You can also deploy scrapy as a daemon, see #http://scrapyd.readthedocs.org/en/latest/

# Sample output
https://github.com/jayzeng/scrapy-stackoverflows/blob/master/jobs.json

# TODO
- Backoff and retry base upon (e.g: http status code)
- A thin web interface to manipulate jobs (schedule, cancel jobs etc)
- Add more spiders and crawlers to cover other job boards
- Deploy it as a real-time API that returns job JSON
- Basic machine learning with PredictionIO or Mahout
- Ability to answer basic questions like, what is the top 10 hot jobs in Seattle?
