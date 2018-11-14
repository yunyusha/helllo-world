# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider
from ..items import *
"""

分布式爬虫运行原理
1: 首先启动爬虫,爬虫自动连接redis服务器,之后爬虫处于监听状态
2: redis服务器通过对应的键,将任务提交给爬虫引擎,进而间接存储到调度器
3: 爬虫引擎将调度器中的任务直接提交给处于空闲状态的下载器
4: 下载器将数据下载之后提交给对应的爬虫引擎,爬虫引擎此时将对应的结果传递给spider
5: spider负责完成对应数据的解析并且将数据转换成Item实例返回给爬虫引擎
6: 爬虫引擎将Item提交给pipeline最终完成数据的持久化存储

"""
class Spider1Spider(RedisSpider):
    name = 'spider1'
    # 为爬虫定义一个从redis中提取任务的键,此后该爬虫会直接根据该键从链接的redis中提取任务
    redis_key = 'st'
    model_names = ['性感美女', '清纯美眉', '美女校花', '性感车模', '旗袍美女', '明星写真']

    # make_request_from_data和make_requests_from_url作用都是可以帮助开发人员手动设置请求,但是不通之处是
    # 前者获取的请求链接是二进制数据类型,同时请求过程中不存在重复网址的过滤操作.但是后者直接获取的是请求的
    #
    # url,并且请求过程中存在重复链接的过滤操作
    #
    # def make_request_from_data(self, data):
    #     return self.make_requests_from_url(data.decode('utf-8'))

    def make_requests_from_url(self, url):
        index = int(url.split('#')[-1])
        url = url.split('#')[0]
        if index >= len(self.model_names):
            return None

        model_name = self.model_names[index]
        return scrapy.Request(url=url, callback=self.parse, meta={'model_name': model_name})
    def parse(self, response):
        # 获取每一个图片对象的标题,链接和详情链接
        titles = response.xpath('//dl[@class="list-left public-box"]dd/a/img/@alt').extract()
        img_urls = response.xpath('//dl[@class="list-left public-box"]/dd/a/img/@src').extract()
        links = response.xpath('//dl[@class="list-left public-box"]/dd/a/@href').extract()
        min_num = min(len(titles), len(img_urls), len(links))
        # 获取模块名
        model_name = response.meta.get('model_name')
        for i in range(min_num):
            item = Spider7Item()
            item['model_name'] = model_name
            item['img_url'] = img_urls[i]
            item['title'] = titles[i]
            item['link'] = links[i]
            yield item

