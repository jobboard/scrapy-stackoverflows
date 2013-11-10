# Scrapy settings for jobboard project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jobboard'

SPIDER_MODULES = ['jobboard.spiders']
NEWSPIDER_MODULE = 'jobboard.spiders'

# Let's be less aggressive (2 sec)
DOWNLOAD_DELAY = 0.5

# bumped from default 180
DOWNLOAD_TIMEOUT = 360

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobboard (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'jobboard.pipelines.JobCompanyPipeline':300,
}

# DB credentials
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'jobs'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'weblamp442'
