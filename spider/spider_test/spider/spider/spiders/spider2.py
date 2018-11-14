# -*- coding: utf-8 -*-
import scrapy,os,json,re
from ..items import BeautifulGirl

class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['www.mm131.com']
    start_urls = []

    def __init__(self):
        # 打开指定位置文件
        path = os.path.dirname(os.path.dirname(__file__))
        f = open(os.path.join(path, 'girls.json'), 'r')
        girls_dic = json.loads(f.read())
        f.close()
        # 获取所有图片的实例
        for key,value in girls_dic.items(): # for循环遍历字典的用法
            if key == '性感车模':
                for item in value:
                    # 创建所有的BeautifulGirl实例.
                    girl = BeautifulGirl(item)
                    self.start_urls.append(girl)
    # 手动设置页面请求(当爬虫刚刚开始时,执行该方法)
    def start_requests(self):
        for item in self.start_urls:
            yield scrapy.Request(url=item.get("link"), callback=self.parse, meta={'girl': item})
    def parse(self, response):
        # 获取当前详情页的总页码
        totle_page = int(re.findall('\d+', response.xpath('//span[@class="page-ch"]/text()').extract()[0])[0])
        # 获取第一页大图链接
        img_url = response.xpath('//div[@class="content-pic"]/a/img/@src').extract()
        # 存储第一页的大图链接
        item = response.meta.get('girl')
        item['big_imgs'] = img_url
        # 完成当前图片实例中其他页面图片链接的存储
        for i in range(2, totle_page+1):
            yield scrapy.Request(url=item.get("link").replace(".html",'_{0}.html'.format(i)),callback=self.parse_page, meta={'girl': item,'totle_page': totle_page})

    # 定义函数完成对其他页面的解析
    def parse_page(self,response):
        img_url = response.xpath('//div[@class="content-pic"]/a/img/@src').extract()[0]
        item = response.meta.get('girl')
        item.get('big_imgs').append(img_url)
        # 判断当前页面数据是否已经全部获取.
        if response.meta.get('totle_page') == len(item.get('big_imgs')):
            yield item

