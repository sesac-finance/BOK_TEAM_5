# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class NewscrawlerItem(scrapy.Item):
    title = scrapy.Field()   # 제목
    content = scrapy.Field()   # 내용
    date = scrapy.Field()   # 날짜
    pass