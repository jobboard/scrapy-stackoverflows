# Stackoverflow Career (Job & Companies) scrapper

Quick n Dirty implementation with scrappy to scrap all jobs and companies on http://careers.stackoverflow.com/jobs

# Sample output
https://github.com/jayzeng/scrapy-stackoverflows/blob/master/jobs.json

# How to run
➜  scrapy-stackoverflows git:(master) ✗ scrapy list
stackoverflowjob
stackoverflowcompany

➜  scrapy-stackoverflows git:(master) ✗ scrapy crawl stackoverflowjob -o test.json -t json

You can also deploy scrapy as a daemon, see #http://scrapyd.readthedocs.org/en/latest/
