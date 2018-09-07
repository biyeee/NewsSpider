# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class NewsspiderItem(scrapy.Item):
    News = Field()  # 新闻
    NewsUrl = Field()
    kind = Field()
    Finance = Field()  # 财经
    Science = Field()  # 科技
    Sports = Field()  # 体育
    Entertainment = Field()  # 娱乐
    Cars = Field()  # 汽车
    Fshion = Field()  # 时尚
    Tourism = Field()  # 旅游
    Real_estate = Field()  # 房产
    Education = Field()  # 教育
    Games = Field()  # 游戏
    Food = Field()  # 美食
