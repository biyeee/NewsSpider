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
        print(URL1)
        # Title = response.xpath('//div[@class="main-nav"]/div/ul/li/a/b/text()').extract()
        for url in URL1:
            yield Request(url, callback=self.parseList, dont_filter=True)

    def parseList(self, response):
        result = re.findall(r'//(.*?).sina.com.cn', response.url)
        if result in self.sub:
            print(result)
