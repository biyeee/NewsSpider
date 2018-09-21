# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from NewsSpider.items import SinaspiderItem
from scrapy_redis.spiders import RedisSpider


class NewSpider(RedisSpider):
    name = 'sina'
    # allowed_domains = ['news.sina.com.cn']
    # start_urls = ['https://news.sina.com.cn/']
    redis_key = 'NewSpider:start_urls'
    sub = [['news'], ['finance'], ['sports'], ['ent'], ['auto'], ['fashion'], ['edu'], ['travel'], ['games'],
           ['tech']]

    def parse(self, response):
        URL = response.xpath('//div[@class="main-nav"]/div/ul/li[1]/a/@href').extract()
        sub = self.sub
        for url in URL:
            result = re.findall(r'//(.*?).sina.com.cn', url)
            for i in sub:
                if result == i:
                    yield Request(url, callback=self.parse2, meta={'result': result}, dont_filter=True)  # 回调所需的url

    def parse2(self, response):
        hrefs = response.xpath('//a[contains(@href,".shtml")]/@href').extract()
        result = response.meta['result']
        for href in hrefs:
            if href.startswith('//'):
                href2 = 'http:' + href
                yield Request(url=href2, callback=self.parse3, meta={'result': result}, dont_filter=True)
            else:
                yield Request(url=href, callback=self.parse3, meta={'result': result}, dont_filter=True)

    def parse3(self, response):
        item = SinaspiderItem()
        title = response.xpath('//h1[@class|id="main-title"]/text()|//div[@class="page-header"]/h1/text()|'
                               '//h1[@id="artibodyTitle"]/text()|//div[@class="new_hot_tit"]/span/text()|'
                               '//div[@class="article-header clearfix"]/h1/text()|'
                               '//div[@class="breadcrumb"]/h1/text()').extract()
        result = response.meta['result']
        if len(title) != 0:
            item['kind'] = result[0]
            item['NewsUrl'] = response.url
            item['News'] = title[0]
            item['Origin'] = '新浪'
            yield item
