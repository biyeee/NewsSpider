# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import redis


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        print("this is request ip:" + proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        # 连接数据库
        r = redis.Redis(host="127.0.0.1", port=6379, password="")
        l = r.hkeys("useful_proxy")
        proxies = []
        for i in l:
            temp = i.decode()
            proxies.append("http://" + temp)
        proxy = random.choice(proxies)
        return proxy
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
