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
                  'https://lol.qq.com/data/info-spell.shtml#Navi']

    def start_requests(self):
        titles = ['英雄', '物品', '召唤师技能']
        for i in range(len(titles)):
            url = self.start_urls[i]
            # if i == 0:
            #     return self.parse_hero(url)
            if i == 1:
                yield self.parse_shop(url)
            else:
                pass

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

                        path = os.path.dirname(__file__)
                        path = os.path.join(path,'img')
                        f = open(os.path.join(path, '{0}.png'.format(small_kind)), 'wb+')
                        f.write(base64.b64decode(hl))
                        f.close()

                        # et = etree.HTML(hl)
                        # img_url = et.xpath('//ul[@id="jSearchItemDiv"]/li/img/@src')
                        # titles = et.xpath('//ul[@id="jSearchItemDiv"]/li/p/text()')
                        # big_kinds = et.xpath('//li[@class="selete-item current"]/label/text()')[0]
                        # small_kinds = et.xpath('//li[@class="selete-item current"]/label/text()')[-1]

                        # print(''.center(50, '='))
                        # print(big_kinds)
                        # print(small_kinds)
                        # print(''.center(50, '='))


        else:
            pass


    # 完成英雄页面的爬去


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
        yield SplashRequest()