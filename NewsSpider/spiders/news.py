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
        sub = self.sub
        for url in URL1:
            result = re.findall(r'//(.*?).sina.com.cn', url)
            for i in sub:
                if result == i:
                    yield Request(url, callback=self.parse2, meta={'result': result}, dont_filter=True)  # 回调所需的url

    def parse2(self, response):
        href = response.xpath('//a[contains(@href,".shtml")]/@href').extract()
        result = response.meta['result']
        for i in href:
            yield Request(i, callback=self.parse3, meta={'result': result},dont_filter=True)

    def parse3(self, response):
        item = NewsspiderItem()
        title = response.xpath('//h1[@class="main-title"]/text()|//div[@class="page-header"]/text()|'
                               '//h1[@id="artibodyTitle"]/text()').extract()
        result = response.meta['result']
        item['kind'] = result[0]
        item['NewsUrl'] = response.url
        item['News'] = title
        yield item
