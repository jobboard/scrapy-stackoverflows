from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from jobboard.items import JobItem, JobUrltem, CompanyUrlItem, CompanyItem

class StackoverflowSpider(CrawlSpider):
    name = 'stackoverflowcompany'
    allowed_domains = ['careers.stackoverflow.com']
    start_urls = ['http://www.careers.stackoverflow.com/jobs/companies?pg=%d' % page
                   for page in xrange(1,158) ]

    rules = (
        #Rule(SgmlLinkExtractor(allow=r'jobs/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        companies = Selector(response).xpath('//div[@id="content"]/div/div[@class="list companies"]/div')

        for company in companies:
            item = CompanyUrlItem()
            item['title'] = company.xpath("p/text()").extract()
            item['location'] = company.xpath('p[@class="location"]').extract()
            uri = company.xpath("a/@href").extract()
            item['link']  = uri
            url = 'http://careers.stackoverflow.com%s' % uri[0]

            yield Request(url= url,
                          meta={'item':item},callback=self.parse_companyurl)

    def parse_companyurl(self, response):
        selector = Selector(response)

        company_details = selector.xpath("//div[@id='company-profile']")

        company_item = CompanyItem()
        company_item['ad_img']    = company_details.xpath('div[@data-company-section="top-image"]/img/@src').extract()
        company_item['logo']      = company_details.xpath('div[@data-company-section="company-info"]/div[@class="logo-container"]/table/tr/td/img/@src').extract()
        company_item['name']      = company_details.xpath('div[@data-company-section="company-info"]/h1/text()').extract()
        company_item['tag_line']  = company_details.xpath('div[@data-company-section="company-info"]/span[@class="tag-line"]/text()').extract()

        # @TODO size, status, and founded year need to be more dynamic,
        # since their orders can be different in each company profile page
        company_item['status']           = company_details.xpath('div[@data-company-section="company-info"]/div[@class="right"]/table/tr[2]/td[2]/text()').extract()
        company_item['statements']       = company_details.xpath('div[@data-company-section="company-statement"]').extract()
        company_item['tech_stack']       = company_details.xpath('div[@data-company-section="tech-stack"]/*[not(self::div[@class="tags"])]').extract()
        company_item['tech_stack_tags']  = company_details.xpath('div[@data-company-section="tech-stack"]/div[@class="tags"]/span/text()').extract()
        company_item['benefits']         = company_details.xpath('div[@data-company-section="benefits"]/div[@class="benefits-list"]/span/@title').extract()


        return company_item
