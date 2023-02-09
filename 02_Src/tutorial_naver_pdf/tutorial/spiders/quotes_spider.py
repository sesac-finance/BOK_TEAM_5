# scrapy의 tutorial/tutorial/spiders/quotes_spider.py 의 경로에 넣어서 사용필요

import scrapy
from  bs4 import BeautifulSoup
import requests


class QuotesSpider(scrapy.Spider):
    name = "naver_pdf_crawler"

    def start_requests(self):
        urls = []
        for i in range (1,148):
            url = f'https://finance.naver.com/research/debenture_list.naver?&page={i}'
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        r = response.text
        soup = BeautifulSoup(r,'html.parser')
        # download link
        file = soup.select('a[href*=".pdf"]')
        link_list=[file[i].attrs['href'] for i in range(30)]
        # subject 
        title = soup.select('a[href^="debenture_read.naver"]')
        subject_list=[title[i].text for i in range(30)]
        # date
        date = soup.select('.box_type_m .date')
        date_list=[date[i].text for i in range(len(date)) if i%2 ==0]

        
        for i in range(30):
            subject=f'{subject_list[i]}_{date_list[i]}.pdf'
    
            with open(subject, "wb") as file:  
                    response = requests.get(link_list[i])
                    file.write(response.content)