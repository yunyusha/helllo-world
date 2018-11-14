# -*- coding: utf-8 -*-

import scrapy,time,os,json,re
from ..items import *



class Spider2Spider(scrapy.Spider):
    # 设置爬虫的名字,用来区分不同爬虫的
    name = 'spider2'
    # 设置当前爬虫允许爬取的网络链接
    allowed_domains = ['www.mm131.com']
    # 完成爬虫初试下载页面的链接设置
    start_urls = []

    # # 当网页下载成功之后需要执行的回调函数,主要完成网页数据的解析
    # def parse(self, response):
    #     pass
    #
    def __init__(self):
        # 打开指定位置的文件.
        path = os.path.dirname(os.path.dirname(__file__))
        f = open(os.path.join(path, 'girls.json'), 'r')
        girls_dic = json.loads(f.read())
        f.close()
        # 获取所有的图片实例.
        for key, value in girls_dic.items():
            if key == '旗袍美女':
                for item in value:
                    # 创建所有的BeautifulGirl实例.
                    girl = BeautifulGirl(item)
                    self.start_urls.append(girl)


    # 手动设置起始请求(当爬虫刚刚开启时,执行该方法)
    def start_requests(self):
        for item in self.start_urls:
            yield scrapy.Request(url=item.get('link'),callback=self.parse,meta={'girl':item})
    def parse(self, response):
        # 获取当前详情页的总页码
        totle_page = re.findall('\d+',response.xpath('//span[@class="page-ch"]/text()').extract()[0])[0]
        totle_page = int(totle_page)
        # 获取第一页大图的链接
        img_url = response.xpath('//div[@class="content-pic"]/a/img/@src').extract()
        # 存储第一页大图链接
        item = response.meta.get('girl')
        item['big_imgs'] = img_url
        # 完成当前图片实例其他页面图片链接的存储
        for i in range(2, totle_page+1):
            yield scrapy.Request(url=item.get('link').replace(".html","_{0}.html".format(i)), callback=self.parse_page,meta={'girl':item,'totle_page':totle_page})

    # 定义函数完成对其他页面数据的解析
    def parse_page(self, response):

        # 获取图片链接
        img_url = response.xpath('//div[@class="content-pic"]/a/img/@src').extract()[0]
        item = response.meta.get('girl')
        item.get('big_imgs').append(img_url)
        # print(item)
        # 判断当前页面数据是否全部获取
        if response.meta.get('totle_page') == len(item.get('big_imgs')):
            yield item



