# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from NewsSpider.items import NewsspiderItem

class NewSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['https://news.sina.com.cn/']
    sub = [['video'], ['news'], ['finance'], ['sports'], ['ent'], ['auto'], ['fashion'], ['edu'], ['travel'], ['games'],
           ['tech']]

    def parse(self, response):
        URL1 = response.xpath('//div[@class="main-nav"]/div/ul/li[1]/a/@href').extract()
        # Title = response.xpath('//div[@class="main-nav"]/div/ul/li/a/b/text()').extract()
        for url in URL1:
            yield Request(url, callback=self.parseList, dont_filter=True)

    def parseList(self, response):
        item = NewsspiderItem()
        result = re.findall(r'//(.*?).sina.com.cn', response.url)
        if result == ['news']:
            href = response.xpath('//a[contains(@href,".shtml")]/@href').extract()
            href2 = response.xpath('//a[contains(@href,".shtml")]/text()').extract()
            print(href)
            print(href2)
            for i in range(len(href)):
                item['NewsUrl'] = href[i]
                item['News'] = href2[i]
                yield item

    # def parse2(self, response):
    #     print(response)

