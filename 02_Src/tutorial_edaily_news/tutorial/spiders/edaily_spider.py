

import scrapy
import sys
from scrapy.spiders import Spider
#from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.selector import Selector
import re
#reload(sys)
#sys.setdefaultencoding('utf-8')

#items.py import 해야할 경우 절대경로를 사용한 path추가 방법 사용
sys.path.insert(0,'C:/Users/codejisu/Desktop/my_BOK/tutorial/tutorial')
from items import edailyCrawlerItem

class edailyCrawler(scrapy.Spider):
    name = "edailyCrawler" #고유한 이름 부여

    def start_requests(self):
        for i in range(1,167): #페이지수
            yield scrapy.Request('https://www.edaily.co.kr/search/news/?source=total&keyword=%ed%86%b5%ed%99%94%ec%a0%95%ec%b1%85&include=&exclude=&jname=&start=20150101&end=20151231&sort=latest&date=pick&exact=false&page={0}'.format(i),self.parse)

    def parse(self, response):
        for i in range(1,21): # 한 페이지 당 기사 20개
            page = f'//*[@id="newsList"]/div[{i}]'
            
            for colum in  response.xpath(f'//*[@id="newsList"]/div[{i}]') :
                item = edailyCrawlerItem()
                item['title'] = colum.xpath(f'//*[@id="newsList"]/div[{i}]/a/ul/li[1]/text()').extract()
                item['date'] = colum.xpath(f'//*[@id="newsList"]/div[{i}]/div/text()')[0].extract()
                item['contents'] = colum.xpath(f'//*[@id="newsList"]/div[{i}]/a/ul/li[2]/text()').extract()
                yield item

