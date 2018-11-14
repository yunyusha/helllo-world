# -*- coding: utf-8 -*-
import scrapy,os,json
from ..items import *
from scrapy_splash import SplashRequest
from lxml import etree
from .lua_js import *
import lxml,base64


class WpSpider(scrapy.Spider):
    name = 'wp'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/data/info-item.shtml#Navi/']

    def start_requests(self):
        url = self.start_urls[0]
        return self.res_operate(url)
    def parse(self, response):
        dic = json.loads(response.body)
        p = 0
        for key,value in dic.items():
            for small_kind, hl in value.items():
        #         et = etree.HTML(hl)
        #         img_urls = et.xpath('//ul[@id="jSearchItemDiv"]/li/img/@src')
        #         titles = et.xpath('//ul[@id="jSearchItemDiv"]/li/p/text()')
        #         big_kinds = et.xpath('//li[@class="selete-item current"]/label/text()')[0]
        #         big_kinds1 = key
        #         small_kinds = small_kind
        #         # small_kinds = et.xpath('//li[@class="selete-item current"]/label/text()')[-1]
        #         print('+++++++++++++++')
        #         print(big_kinds)
        #         print(big_kinds1)
        #         print(small_kinds)
        #         p = p + 1
        #         # print(titles)
        #         # print(img_urls)
        #         print('+++++++++++++++')
        # print('--------------')
        # print(p)

                path = os.path.dirname(__file__)
                path = os.path.join(path,'img')
                f = open(os.path.join(path, '{0}.png'.format(small_kind)), 'wb+')
                f.write(base64.b64decode(hl))
                f.close()

        # print(dic)

    # 定义函数完成爬取物品页面的数据
    def res_operate(self,url):
        defence = {'生命值': 'health', '生命回复': 'healthregen', '护甲': 'armor', '魔法抗性': 'spellblock'}
        attack = {'生命偷取': 'lifesteal', '暴击': 'criticalstrike', '攻击速度': 'attackspeed', '攻击力': 'damage'}
        magic = {'法力值': 'mana', '法术强度': 'spelldamage', '冷却强度': 'cooldownreduction', '法力回复': 'manaregen'}
        movement = {'鞋子': 'boots', '其他移动速度物品': 'nonbootsmovement'}
        consumable = {}
        dic = {'defence': defence , 'attack': attack, 'magic': magic, 'movement': movement, 'consumable': consumable}
        self.dic_1 = dic
        yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source': lua_res, 'wait': 3, 'kind_dic': dic, 'model_name': '物品'})




