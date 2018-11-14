# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.conf import settings
from scrapy import Request


class DB:
    def start_connect(self):
        client = pymongo.MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]
        self.col = self.db[settings['MONGO_COLNAME']]

    # 判断数据是否存在
    def or_exist(self, title):
        result = self.col.find({'title': title}).count()
        if result != 0:
            return True
        else:
            return False

    # 过滤数据库存储时的重复
    def or_repeat(self, **kwargs):
        result = self.col.find(kwargs).count()
        if result != 0:
            return True
        else:
            return False


class Spider6Pipeline(object):
    def process_item(self, item, spider):
        return item


class DownloadImage(ImagesPipeline, DB):
    def get_media_requests(self, item, info):
        if not hasattr(self, 'col'):
            self.start_connect()
        dic = dict(item)
        if self.or_exist(dic['title']) is False:
            img_url = dic['img_url']
            img_list = []
            if 'big_img' in dic.keys():
                big_img = dic['big_img']
                big_img = 'http:' + big_img
                img_list.append(big_img)
            if img_url.startswith('http') is False:
                img_url = 'http:'+img_url
                img_list.append(img_url)
                if item['model_name'] == '英雄':
                    dirname = 'hero'
                elif item['model_name'] == '物品':
                    dirname = 'shop'
                elif item['model_name'] == '召唤师技能':
                    dirname = 'skill'
                for i in range(len(img_list)):
                    print(''.center(50, '='))
                    print(img_list[i])
                    print(''.center(50, '*'))
                    yield Request(url=img_list[i], meta={'dir_name': dirname,
                                                 'img_name': img_list[i].split('/')[-1]})
    # 设置图片下载成功之后图片下载的路径
    def file_path(self, request, response=None, info=None):
        # 获取文件和文件夹名
        dirname = request.meta['dir_name']
        img_name = request.meta['img_name']

        return '{0}/{1}'.format(dirname, img_name)

    # 当图片下载完成之后修改数据源的链接
    def item_completed(self, results, item, info):
        if item['model_name'] == '英雄':
            dirname = 'hero'
        elif item['model_name'] == '物品':
            dirname = 'shop'
        elif item['model_name'] == '召唤师技能':
            dirname = 'skill'
        # 获取item图片名
        img_name = item['img_url'].split('/')[-1]
        item['img_url'] = 'http://127.0.0.1:8080/img/{0}/{1}'.format(dirname, img_name)
        if 'big_img' in dict(item):
            img_name = item['big_img'].split('/')[-1]
            item['big_img'] = 'http://127.0.0.1:8080/img/{0}/{1}'.format(dirname, img_name)

        # 将数据存入数据库
        if item['model_name'] == '英雄':
            if self.or_repeat(**{'title': item['title'],
                                 'kind': item['kind']}) is False:
                self.col.insert(dict(item))
        elif item['model_name'] == '物品':
            # 新建数据库集合
            self.col = self.db['shop_page']
            if self.or_repeat(**{'title': item['title'], 'big_kind': item['big_kind'],
                                 'small_kind': item['small_kind']}) is False:
                self.col.insert(dict(item))
        elif item['model_name'] == '召唤师技能':
            self.col = self.db['skill']
            if self.or_repeat(**{'title': item['title']}) is False:
                self.col.insert(dict(item))
        return item