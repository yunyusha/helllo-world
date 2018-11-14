# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os,json
class SpiderPipeline(object):
    def __init__(self):
        self.girl_dic = {}
    def process_item(self, item, spider):
        dic = dict(item)
        if spider.name == 'spider1':
            model_name = dic['model_name']
            if model_name not in self.girl_dic:
                self.girl_dic[model_name] = [dic]
            else:
                self.girl_dic[model_name].append(dic)

    # 爬虫关闭时执行
    def close_spider(self, spider):
        if spider.name == 'spider1':
            f = open(os.path.join(os.path.dirname(__file__), 'girls.json'),'w')
            f.write(json.dumps(self.girl_dic))
            f.close()