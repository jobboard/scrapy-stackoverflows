# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JobUrltem(Item):
    title = Field()
    link  = Field()

class JobItem(Item):
    about         = Field()
    desc          = Field()
    employer      = Field()
    employer_link = Field()
    joeltest      = Field()
    location      = Field()
    skills        = Field()
    tags          = Field()
    title         = Field()

class CompanyUrlItem(Item):
    title    = Field()
    link     = Field()
    location = Field()

class CompanyItem(Item):
    ad_img          = Field()
    benefits        = Field()
    # @TODO currently not used
    founded_year    = Field()
    logo            = Field()
    name            = Field()
    statements      = Field()
    status          = Field()
    tag_line        = Field()
    tech_stack      = Field()
    tech_stack_tags = Field()
