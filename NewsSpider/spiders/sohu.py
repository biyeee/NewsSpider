# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from NewsSpider.items import SohuspiderItem


class SohuSpider(RedisSpider):
    name = 'sohu'
    # allowed_domains = ['news.sohu.com']
    # start_urls = ['http://news.sohu.com/']
    redis_key = 'SohuSpider:start_urls'
    sub = [['news'], ['business'], ['sports'], ['yule'], ['auto'], ['fashion'], ['it'], ['travel'], ['game'],
           ['learning']]

    def parse(self, response):
        URL = response.xpath('//div[@class="head-nav left"]/ul/li/a/@href|//div[@class="more-nav-box"]/a/@href').extract()
        sub = self.sub
        for url in URL:
            result = re.findall(r'//(.*?).sohu.com', url)
            for i in sub:
                if result == i:
                    yield Request(url, callback=self.parse2, meta={'result': result}, dont_filter=True)

    def parse2(self, response):
        hrefs = response.xpath('//a[contains(@href,"www.sohu.com/a/")]/@href').extract()
        result = response.meta['result']
        for href in hrefs:
            if href.startswith('//'):
                href2 = 'http:' + href
                yield Request(url=href2, callback=self.parse3, meta={'result': result}, dont_filter=True)
            else:
                yield Request(url=href, callback=self.parse3, meta={'result': result}, dont_filter=True)

    def parse3(self, response):
        item = SohuspiderItem()
        title = response.xpath('//div[@class="text-title"]/h1/text()|//h3[@class="article-title"]/text()').extract()
        result = response.meta['result']
        if len(title) == 0:
            print("no title")
        else:
            res = re.findall(r'\S+', title[0])
            total = ''
            for i in res:
                total = total + i  # 匹配文字并且拼接（去除空格和换行符）
            item['kind'] = result[0]
            item['NewsUrl'] = response.url
            item['News'] = total
            item['Origin'] = '搜狐'
            yield item
