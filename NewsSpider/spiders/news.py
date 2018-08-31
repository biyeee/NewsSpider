# -*- coding: utf-8 -*-
import scrapy


class NewSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['https://news.sina.com.cn/']

    def parse(self, response):
        URL1 = response.xpath('//div[@class="main-nav"]/div/ul/li[1]/a/@href').extract()
        Title = response.xpath('//div[@class="main-nav"]/div/ul/li/a/b/text()').extract()
        print(URL1)
        print(Title)
