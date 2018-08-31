# -*- coding: utf-8 -*-
import scrapy


class NewSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['https://news.sina.com.cn/']

    def parse(self, response):
        print(response)
