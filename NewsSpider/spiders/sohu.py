# -*- coding: utf-8 -*-
import scrapy


class SohuSpider(scrapy.Spider):
    name = 'sohu'
    allowed_domains = ['news.sohu.com']
    start_urls = ['http://news.sohu.com/']

    def parse(self, response):
        pass
