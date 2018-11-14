# -*- coding: utf-8 -*-
import scrapy,os,json
from ..items import *
# 专门用来生成基于Splash加载的网络请求
from scrapy_splash import SplashRequest
from lxml import etree
from .lua_js import *
import base64
import lxml
# 定义一段lua脚本控制页面行为
script1 = """
       
"""


class ZlSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/data/info-heros.shtml#Navi','http://lol.qq.com/data/info-item.shtml#Navi','http://lol.qq.com/data/info-spell.shtml#Navi']

    def start_requests(self):
        titles = ['英雄', '物品', '召唤师技能']
        for i in range(len(titles)):
            url = self.start_urls[i]
            return self.hero_operate(url)


    def parse(self, response):
        dic = json.loads(response.body)

        if dic['model_name'] == '英雄':
            # for key,value
            et = etree.HTML(dic['data'])
            img_urls = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/img/@src')
            links = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href')
            titles = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/p/text()')
            for i in range(len(titles)):
                hero = Hero()
                hero['model_name'] = '英雄'
                hero['kind'] = dic['kind']
                hero['img_url'] = img_urls[i]
                hero['link'] = links[i]
                hero['title'] = titles[i]
                yield hero


    # 定义函数完成爬取英雄页面的数据
    def hero_operate(self, url):
        dic = {'Fighter': '战士', 'Mage': '法师', 'Assassin': '刺客', 'Tank': '坦克', 'Marksman': '射手', 'Support': '辅助'}



        yield SplashRequest(url=url, callback=self.parse,endpoint='execute', args={'lua_source': lua_hero, 'waite': 7,'kind_dic': dic, 'model_name': '英雄'})




