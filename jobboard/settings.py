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

SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# Let's be less aggressive (2 sec)
DOWNLOAD_DELAY = 0.5
DNSCACHE_ENABLED = True

# bumped from default 180
DOWNLOAD_TIMEOUT = 360

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':100,
    'jobboard.pipelines.JobCompanyPipeline':200,
}

COMMANDS_MODULE = 'jobboard.commands'

LOG_FILE = 'stackoverflow.log'

# DB credentials
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'jobs'
MYSQL_USER = ''
MYSQL_PASSWD = ''

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN =8
