# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


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


class NewSpiderLoader(ItemLoader):
    default_item_class = SinaspiderItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()


class IfengSpiderLoader(ItemLoader):
    default_item_class = IfengspiderItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()


class SohuSpiderLoader(ItemLoader):
    default_item_class = SohuspiderItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()