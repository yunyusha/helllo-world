# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class Spider7Pipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGO_HOST'], settings['MONGO_PORT'])
        db = client[settings['MONGO_DB']]
        self.col = db[settings['MONGO_COLNAME']]


    def process_item(self, item, spider):
        if self.col.find({'title': item['title']}).count() == 0:
            self.col.insert(dict(item))
        return item
