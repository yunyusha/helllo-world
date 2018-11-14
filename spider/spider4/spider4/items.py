# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
items.py : 用来设置未来存储数据的数据源,在该文件中所有的数据源必须继承自scrapy.item, 该数据源作用与
django中models.py类似,但是不同之处是,该数据源中提供的数据没有django中丰富的数据类型,所有数据都是
Field类型,并且该数据源未来构造的实例并不是对象实例,而是字典类型的实例
"""
class BeautifulGirl(scrapy.Item):
    model_name = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    big_imgs =scrapy.Field()
