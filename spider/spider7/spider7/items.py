# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider7Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model_name = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()

class Hero(scrapy.Item):
    model_name = scrapy.Field()
    kind = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    link = scrapy.Field()

class Shop(scrapy.Item):
    model_name = scrapy.Field()
    big_kind = scrapy.Field()
    small_kind = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()

class Skill(scrapy.Item):
    model_name = scrapy.Field()
    title = scrapy.Field()
    level = scrapy.Field()
    big_img = scrapy.Field()
    des = scrapy.Field()
    img_url = scrapy.Field()
