# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class SinaspiderItem(scrapy.Item):
    News = Field()  # 新闻
    NewsUrl = Field()  # 新闻链接
    kind = Field()  # 新闻类型
    Origin = Field()  # 来源

class SohuspiderItem(scrapy.Item):
    News = Field()  # 新闻
    NewsUrl = Field()  # 新闻链接
    kind = Field()  # 新闻类型
    Origin = Field()  # 来源

class IfengspiderItem(scrapy.Item):
    News = Field()  # 新闻
    NewsUrl = Field()  # 新闻链接
    kind = Field()  # 新闻类型
    Origin = Field()  # 来源

