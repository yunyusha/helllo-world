# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo,os

class Spider5Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        #　构建数据库
        db = client[settings['MONGO_DB']]
        # 根据数据库构建对应的集合
        self.col = db[settings['MONGO_COLNAME']]

    def process_item(self, item, spider):
        dic = dict(item)
        self.col.insert(dic)
        return item
