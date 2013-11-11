import urllib
import urllib2
from scrapy import log
from scrapy.command import ScrapyCommand

class AllCrawlCommand(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED':False}

    def short_desc(self):
        return 'Schedule a run for all available spiders'

    def run(self, args, opts):
        # @TODO pull from setting
        url = 'http://localhost:6800/schedule.json'
        crawler = self.crawler_process.create_crawler()
        spiders = crawler.spiders.list()

        for spider in spiders:
            values = {'project':'default', 'spider':spider}
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            # @TODO log differently base upon responses
            log.msg(response)
