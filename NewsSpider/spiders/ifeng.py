# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy import Request

from NewsSpider.items import IfengspiderItem


class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/']
    sub = [['news'], ['finance'], ['sports'], ['ent'], ['auto'], ['fashion'], ['tech'], ['travel'], ['games'],
           ['book']]


    def parse(self, response):
        URL = response.xpath('//div[@class="h_mainNavNew cDGray h_mainNav"]/ul/li/a/@href').extract()
        sub = self.sub
        for url in URL:
            result = re.findall(r'//(.*?).ifeng.com', url)
            for i in sub:
                if result == i:
                    url = "http:" + url
                    yield Request(url, callback=self.parse2, meta={'result': result}, dont_filter=True)

    def parse2(self, response):
        hrefs = response.xpath('//a[contains(@href,".shtml")]/@href').extract()
        result = response.meta['result']
        for href in hrefs:
            if href.startswith('//'):
                href2 = 'http:' + href
                yield Request(url=href2, callback=self.parse3, meta={'result': result}, dont_filter=True)
            else:
                yield Request(url=href, callback=self.parse3, meta={'result': result}, dont_filter=True)
    #
    def parse3(self, response):
        item = IfengspiderItem()
        title = response.xpath('//div[@id="artical"]/h1/text()|//div[@class="titL"]/h1/text()|'
                               '//div[@class="vTit_Inner"]/h2/text()|//div[@class="arl-cont"]/h3/span/text()').extract()
        result = response.meta['result']
        if len(title) != 0:
            res = re.findall(r'\S+', title[0])
            total = ''
            for i in res:
                total = total + i
            item['kind'] = result[0]
            item['NewsUrl'] = response.url
            item['News'] = total
            item['Origin'] = '凤凰新闻'
            yield item
