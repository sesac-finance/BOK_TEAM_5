
import scrapy
from hankyung_news.items import HankyungNewsItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = []
        try:
            for i in range(1,5818):
                url = f"https://search.hankyung.com/apps.frm/search.news?query=금리&sort=DATE%2FDESC%2CRANK%2FDESC&period=DATE&area=ALL&mediaid_clust=HKPAPER%2CHKCOM&sdate=20110101&edate=20221011&exact=&include=&except=&page={i}"
                urls.append(url)
        except:
            pass
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url_links =[f'//*[@id="content"]/div[1]/div/div[1]/div/ul/li[{i}]/div/a/@href' for i in range(1,11)]

        for url_link in url_links:
            try:
                url = response.xpath(url_link)[0].extract()
                yield scrapy.Request(url=url, callback=self.parse_page_content)
            except:
                pass

    def parse_page_content(self, response):
        print(response.xpath('//*[@id="container"]/div/div/article/h1/text()')[0].extract().strip())
        item = HankyungNewsItem()
        item['title'] = response.xpath('//*[@id="container"]/div/div/article/h1/text()')[0].extract().strip()
        item['date'] = response.xpath('//*[@id="container"]/div/div/article/div/div/div[2]/div[1]/span[1]/span/text()')[0].extract().split(' ')[0]
        contents = response.xpath('//*[@id="articletxt"]/text()').extract()
        item['content'] = [''.join(contents[i].strip()) for i in range(len(contents))]
        # item['content'] = response.xpath('//*[@id="articletxt"]/text()').extract()
        yield item


    







    #     for crawled_url in self.crawled_urls :
    #         yield scrapy(url=crawled_url, callback=self.parse_link)
            

    # def parse_link(self, response):
    #     print(response.text)