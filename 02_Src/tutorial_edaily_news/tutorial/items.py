# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class edailyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #기사 제목
    title = scrapy.Field()
    
    #작성 날짜
    date = scrapy.Field()

    #기사 내용
    contents = scrapy.Field()

