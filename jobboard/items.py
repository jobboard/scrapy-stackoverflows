# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JobUrltem(Item):
    title = Field()
    link  = Field()

class JobItem(Item):
    title    = Field()
    employer = Field()
    employer_link = Field()
    location = Field()
    company  = Field()
    desc     = Field()
    skills   = Field()
    about    = Field()
    joeltest = Field()
