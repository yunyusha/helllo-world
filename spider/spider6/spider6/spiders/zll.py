# -*- coding: utf-8 -*-
import scrapy,os,json
from ..items import *
#SplashRequest专门用来生成基于splash的网络数据请求.
from scrapy_splash import SplashRequest
from lxml import etree
from .lua_js import *

class ZLSpider(scrapy.Spider):
    name = 'zll'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/data/info-heros.shtml',
                  'https://lol.qq.com/data/info-item.shtml#Navi',
                  'https://lol.qq.com/data/info-spell.shtml#Navi']

    def start_requests(self):
        titles = ['英雄', '物品', '召唤师技能']
        for i in range(len(titles)):
            url = self.start_urls[i]
            return self.hero_operate(url)

    def parse(self, response):
        dic = json.loads(response.body)
        if dic['model_name'] == '英雄':
            for key,value in dic.items():
                if key != 'model_name':
                    et = etree.HTML(value)
                    img_urls = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/img/@src')
                    links = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href')
                    titles = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/p/text()')
                    for i in range(len(titles)):
                        hero = Hero()
                        hero['model_name'] = '英雄'
                        hero['kind'] = key
                        hero['img_url'] = img_urls[i]
                        hero['link'] = links[i]
                        hero['title'] = titles[i]
                        yield hero


    #定义函数完成爬取英雄页面的数据.
    def hero_operate(self,url):
        dic = {'Fighter':'战士','Mage':'法师','Assassin':'刺客','Tank':'坦克','Marksman':'射手','Support':'辅助'}
        yield SplashRequest(url=url, callback=self.parse,endpoint='execute',args={'lua_source':luo_hero,'wait':7, 'kind_dic':dic, 'model_name':'英雄'})

    #定义函数完成

