from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from jobboard.items import JobItem, JobUrltem

class StackoverflowSpider(CrawlSpider):
    name = 'stackoverflow'
    allowed_domains = ['careers.stackoverflow.com']
    start_urls = ['http://www.careers.stackoverflow.com/jobs?pg=%d' % page
                   for page in xrange(74) ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'jobs/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        jobs = Selector(response).xpath('//div[@class="can-apply"]')

        for job in jobs:
            item = JobUrltem()
            item['title'] = job.xpath("h3/a/@title").extract()
            url = job.xpath("h3/a/@href").extract()
            item['link']  = url
            url = 'http://careers.stackoverflow.com/%s' % url[0]

            yield Request(url= url,
                          meta={'item':item},callback=self.parse_joburl)

    def parse_joburl(self, response):
        selector = Selector(response)

        job_detail = selector.xpath("//div[@class='jobdetail']")

        job_item = JobItem()
        job_item['title'] = job_detail.xpath("div[@id='hed']/h1/a/text()").extract()
        job_item['employer'] = job_detail.xpath("div[@id='hed']/h1/a/@href").extract()
        job_item['employer_link'] = job_detail.xpath("div[@id='hed']/a[@class='employer']/@href").extract()
        job_item['location'] = job_detail.xpath("div[@id='hed']/span[@class='location']/text()").extract()[0].strip("\r\n").strip()
        job_item['desc'] = job_detail.xpath("div[@class='description'][1]").extract()
        job_item['skills'] = job_detail.xpath("div[@class='description'][2]").extract()
        job_item['about'] = job_detail.xpath("div[@class='description'][3]").extract()
        job_item['joeltest'] = job_detail.xpath("ul[@id='joeltest']/li[@class='checked']").extract()

        return job_item
