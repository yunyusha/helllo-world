# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,os
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
# settings对象中存储的是当前爬虫工程中settings文件的所有配置信息,该文件中的
# 所有信息是以键值对的形式存储在对应的settings对象中
from scrapy.conf import settings
import pymongo
"""

pipelines完成对爬虫返回的item数据的处理操作

"""
# 数据库操作类
class DB:
    def start_connect(self):
        # 开始链接MongoDB数据库
        client = pymongo.MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        # 根据链接结果生成指定的数据库
        self.db = client[settings['MONGO_DB']]
        # 根据数据库生成指定的集合
        self.col = self.db[settings['MONGO_COLNAME']]
        # 添加对象方法判断给定的条件对应的数据是否存在
    def not_exist(self, condition):
        result = self.col.find(condition).count()
        if result == 0:
            return True
        else:
            return False



class Spider4Pipeline(DB,object):
    def __init__(self):
        self.girl_dic = {}
        self.start_connect()

    # 用来接收爬虫返回的Item数据
    def process_item(self, item, spider):
        dic = dict(item)
        if spider.name == 'spider1':
            model_name = dic['model_name']
            if model_name not in self.girl_dic:
                self.girl_dic[model_name] = [dic]
            else:
                self.girl_dic[model_name].append(dic)
        else:
            if self.not_exist({'link':item.get('link')}):
                self.col.insert(dic)
        return item

    # 当爬虫关闭时执行
    def close_spider(self,spider):
        if spider.name == "spider1":
            print("------------===================")
            f = open(os.path.join(os.path.dirname(__file__),'girls.json'), 'w')

            f.write(json.dumps(self.girl_dic))
            f.close()

    # 重新定义一个管道类用来处理图片
class DownloadImage(ImagesPipeline,DB):
    # 当爬虫提交items之后执行该操作,通常在此操作中发送图片请求
    def get_media_requests(self, item, info):
        if item.get('big_imgs') is not None:
            # 判断当前DownloadImage对象是否已经链接过数据库,如果没有则执行start_connect完成MongoDB数据库链接
            if not hasattr(self,'col'):
                self.start_connect()
            # 判断当前的item是否已经下载过
            if self.not_exist({'link':item.get('link')}):
                for url in item.get('big_imgs'):
                    page = url.split('/')[-1].split('.')[0]
                    page_html = item.get('link').replace('.html', '_{0}.html'.format(page))
                    header = {'Referer':page_html}
                    yield Request(url=url, meta={'link':item.get('link'),'img_name':url.split("/")[-1]}, headers=header)

    # 设置下载之后的图片的存储路径(代码动态创建的路径)
    def file_path(self, request, response=None, info=None):
        # 获取请求时传输的参数信息
        home_url = request.meta.get('link')
        # 获取图片名字
        img_name = request.meta.get('img_name')
        dir_name = '_'.join( home_url.split('/')[-2:]).replace(".html","")

        return "{0}/{1}".format(dir_name,img_name)

    # item_completed :当每一个item对应的图片下载任务全部结束时调用,通常在该方法中完成指定item的过滤操作
    def item_completed(self, results, item, info):
        for tuple_item in results:
            if tuple_item[0] is True:
                # 获取当前下载的图片链接
                img_url = tuple_item[1].get('url')
                # 获取图片存储的路径
                img_path = tuple_item[1].get('path')
                # 获取图片最新的链接
                new_path = "http://127.0.0.1:8080/img/"+img_path
                # 获取原图链接在big_imgs中的位置下标
                index = item.get('big_imgs').index(img_url)
                item.get('big_imgs')[index] = new_path

        return item


