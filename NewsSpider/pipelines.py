# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql


# class NewsspiderPipeline(object):
#
#     collection_name1 = 'News'
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         self.db[self.collection_name1].update({'NewsUrl': item['NewsUrl']}, dict(item), True)  # 去重
#         return item

class NewsspiderPipeline(object):

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        if spider.name == "sina":
            try:
                self.cursor.execute("""insert into sina(News,NewsUrl,kind,Origin)values("%s","%s","%s","%s")""",
                                    (item['News'], item['NewsUrl'], item['kind'], item['Origin']))
            except:
                pass
        elif spider.name == "sohu":
            try:
                self.cursor.execute("""insert into sohu(News,NewsUrl,kind,Origin)values("%s","%s","%s","%s")""",
                                    (item['News'], item['NewsUrl'], item['kind'], item['Origin']))
            except:
                pass
        elif spider.name == "ifeng":
            try:
                self.cursor.execute("""insert into ifeng(News,NewsUrl,kind,Origin)values("%s","%s","%s","%s")""",
                                    (item['News'], item['NewsUrl'], item['kind'], item['Origin']))
            except:
                pass
        else:
            spider.log('Undefined name:%s' % spider.name)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
