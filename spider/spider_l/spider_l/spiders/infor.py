# -*- coding: utf-8 -*-
import scrapy
import os, json
import base64
from lxml import etree
from .lua_js import *
from ..items import *
from scrapy_splash import SplashRequest



class InforSpider(scrapy.Spider):
    name = 'infor'
    allowed_domains = ['lol.qq.com']
    start_urls = ['https://lol.qq.com/data/info-heros.shtml#Navi',
                  'https://lol.qq.com/data/info-item.shtml#Navi',
                  'https://lol.qq.com/data/info-spell.shtml#Navi'
                  ]

    def start_requests(self):
        titles = ['英雄', '物品', '召唤师技能']
        for i in range(len(titles)):
            url = self.start_urls[i]
            # if i == 0:
            #     return self.parse_hero(url)
            # if i == 1:
            #     return self.parse_shop(url)
            if i == 2:
                return self.parse_skill(url)

    def parse(self, response):
        dic = json.loads(response.body)
        if dic['model_name'] == '英雄':
            for key, value in dic.items():
                if key != 'model_name':
                    et = etree.HTML(value)
                    img_urls = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/img/@src')
                    links = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href')
                    titles = et.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@title')
                    for i in range(len(titles)):
                        hero = Hero()
                        hero['model_name'] = '英雄'
                        hero['kind'] = key
                        hero['img_url'] = img_urls[i]
                        hero['link'] = links[i]
                        hero['title'] = titles[i]
                        yield hero

        elif dic['model_name'] == '物品':
            for key, value in dic.items():
                if key != 'model_name':
                    for small_kind, hl in value.items():
                        et = etree.HTML(hl)
                        img_url = et.xpath('//ul[@id="jSearchItemDiv"]/li/img/@src')
                        titles = et.xpath('//ul[@id="jSearchItemDiv"]/li/p/text()')
                        small_kind = et.xpath('//li[@class="selete-item current"]/label/text()')[1]
                        for i in range(len(titles)):
                            shop = Shop()
                            shop['model_name'] = '物品'
                            shop['big_kind'] = key
                            shop['small_kind'] = small_kind
                            shop['img_url'] = img_url[i]
                            shop['title'] = titles[i]
                            yield shop
            print(''.center(50, '='))
        elif dic['model_name'] == '召唤师技能':
            for key, hl in dic.items():
                if key != 'model_name':
                    et = etree.HTML(hl)
                    skill = Skill()
                    small_img = et.xpath('//div[@class="spell-title"]/img/@src')[0]
                    level = et.xpath('//div[@id="spellDefail"]/div/p/span/text()')[0]
                    des = et.xpath('//div[@class="spell-desc"]/text()')[0]
                    big_img = et.xpath('//div[@id="spellDefail"]/div/img/@src')[1]
                    skill['model_name'] = '召唤师技能'
                    skill['title'] = key
                    skill['img_url'] = small_img
                    skill['level'] = '召唤师等级: {}级'.format(level)
                    skill['des'] = des
                    skill['big_img'] = big_img
                    yield skill

    # 完成英雄页面的爬去
    def parse_hero(self, url):
        dic = {'Fighter': '战士', 'Mage': '法师', 'Assassin': '刺客',
               'Tank': '坦克', 'Marksman': '射手', 'Support': '辅助'}

        yield SplashRequest(url=url, callback=self.parse, endpoint='execute',
                            args={'lua_source': lua_hero, 'wait': 5,
                                  'kind_dic': dic, 'model_name': '英雄'})

    def parse_shop(self, url):
        dic = {'defense':
                     {'type': "防御类", 'health': "生命值",
                        'healthregen': "生命回复", 'armor': "护甲",
                        'spellblock': "魔法抗性"
                    },
              'attack':
                    {'type':"攻击类", 'lifesteal': "生命偷取",
                    'criticalstrike': "暴击",'attackspeed': "攻击速度",
                     'damage': "攻击力"
                    },
              'magic':
                    {'type': "法术类",'mana': "法力值", 'spelldamage': "法术强度",
                    'cooldownreduction': "冷却缩减", 'manaregen': "法力回复"
                    },
              'movement':
                    {'type':"移动速度",'boots': "鞋子",
                    'nonbootsmovement': "其他移动速度物品"
                    },
               'consumable':
                   { 'type': '消耗品',
                     'test': '消耗品'
                    }
               }

        yield SplashRequest(url=url, callback=self.parse, endpoint='execute',
                            args={'lua_source': lua_shop, 'wait': 3, 'model_name': '物品',
                                  "kind_dic": dic})

    def parse_skill(self, url):
        dic = {'1':'屏障', '2':'净化', '3':'引燃', '4':'虚弱', '5': '惩戒',
               '6': '闪现', '7': '幽灵疾步', '8': '治疗术', '9': '清晰术',
               '10': '护驾！', '11': '魄罗投掷',  '12': '标记', '13': '传送'
               }
        yield SplashRequest(url=url, callback=self.parse, endpoint='execute',
                            args={'lua_source': lua_skill1, 'wait': 3, 'model_name': '召唤师技能',
                                 'skill_dic': dic })