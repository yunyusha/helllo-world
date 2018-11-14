# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
items.py 用于设置未来存储数据的数据源,在该文件中所有的数据源必须继承自scarpy.Item. 该数据的作用跟
django中的models比较类似,但是不同之处是,该数据源提供的数据没有django中丰富的数据类型,所以数据类型
都是Filed类型,并且该数据源未来构造的实例并不是对象实例,而是字典实例

"""
class BeautifulGirl(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model_name = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    big_imgs = scrapy.Field()