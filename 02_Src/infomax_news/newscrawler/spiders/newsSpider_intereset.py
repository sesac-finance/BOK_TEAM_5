import scrapy
from bs4 import BeautifulSoup
import requests
import time
import csv
from newscrawler.items import NewscrawlerItem

class NewsUrlSpider(scrapy.Spider):
    name = "newsUrlCrawler"

    def start_requests(self):
        urls = []
        for i in range(1,5769):
            # 검색키워드 : 금리 5768
            url = f'https://news.einfomax.co.kr/news/articleList.html?page={i}&total=173040&box_idxno=&sc_area=A&view_type=sm&sc_section_code=&sc_level=&sc_article_type=&sc_sdate=2008-01-01&sc_edate=2022-10-12&sc_order_by=E&sc_word=%EA%B8%88%EB%A6%AC&sc_andor=OR&sc_word2='
            urls.append(url)
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self,response):
        soup = BeautifulSoup(response.text, 'html.parser')
        urls = soup.select('.list-titles a')   # 기사링크
        
        for i in range(30):
            # print(urls[i].attrs['href'])
            url = 'https://news.einfomax.co.kr'+urls[i].attrs['href']
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_news)

  
    def parse_news(self,response):
        soup2 = BeautifulSoup(response.text, 'html.parser')
        print(soup2.select_one('.article-head-title').text)
        # print(soup2.select_one('#article-view-content-div').text)
        print(soup2.select('.info-text li')[1].text.split(' ')[2])   

        item = NewscrawlerItem()
        item['title'] = soup2.select_one('.article-head-title').text
        item['content'] = soup2.select_one('#article-view-content-div').text        
        item['date'] = soup2.select('.info-text li')[1].text.split(' ')[2]
     
        yield item






# class NewsUrlSpider(scrapy.Spider):
#     name = "newsUrlCrawler"

#     def start_requests(self):
#         urls = []
#         for i in range(1,4):
#             url = f'https://news.einfomax.co.kr/news/articleList.html?page={i}&total=175330&box_idxno=&sc_area=A&view_type=sm&sc_word=%EA%B8%88%EB%A6%AC'
#             urls.append(url)
#         for url in urls:
#             print(url)
#             yield scrapy.Request(url=url, callback=self.parse_news)

#     def parse_news(self, response):
#         soup = BeautifulSoup(response.text,"html.parser")
#         result = soup.select('.list-titles a')
#         url_list =[]
#         for i in range(30):
#             url_list.append('https://news.einfomax.co.kr/'+result[i].attrs['href'])
#         print(url_list)

#         for i in range(len(url_list)):
#             r_2=requests.get(url_list[i])
#             soup2 = BeautifulSoup(r_2.text,'html.parser')
#             title = soup2.select_one('.article-head-title').text
#             item = NewscrawlingItem()
#             item['url'] = soup2.select('#article-view-content-div')