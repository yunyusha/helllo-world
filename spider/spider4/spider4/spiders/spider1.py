# -*- coding: utf-8 -*-

import scrapy,time
from ..items import *


class Spider1Spider(scrapy.Spider):
    # 设置爬虫的名字,用来区分不同爬虫的
    name = 'spider1'
    # 设置当前爬虫允许爬取的网络链接
    allowed_domains = ['www.mm131.com']
    # 完成爬虫初试下载页面的链接设置
    start_urls = ['http://www.mm131.com/']

    # 当网页下载成功之后需要执行的回调函数,主要完成网页数据的解析
    def parse(self, response):
        # response: 下载模块下载的数据extract()将查找之后的结果对象中的数据过滤
        urls = response.xpath('//div[@class="nav"]/ul/li/a/@href').extract()[1:]
        model_names = response.xpath('//div[@class="nav"]/ul/li/a/text()').extract()[1:]
        print("test".center(50, '-'))


        for i in range(len(urls)):
            # time.sleep(2)
            # 生成新的数据请求
            yield scrapy.Request(url=urls[i], meta={'model_name': model_names[i],'url':urls[i]},callback=self.parse_model)

    # 定义函数完成对非主页外的其他页面的数据解析
    def parse_model(self, response):
        print("开始解析".center(50, '-'))
        # 获取美女图片
        girl_infor = response.xpath('//div[@class="main"]/dl/dd/a/img/@src').extract()
        # 和2美女标题
        girl_title  = response.xpath('//div[@class="main"]/dl/dd/a/img/@alt').extract()
        # 获取美女图片详情页的链接
        girl_link = response.xpath('//div[@class="main"]/dl/dd/a/@href').extract()
        length = min(len(girl_title), len(girl_infor), len(girl_link))
        # 将数据构建成BeautifulGirl实例
        for i in range(length):
            girl = BeautifulGirl()
            girl['model_name'] = response.meta['model_name']
            girl['img_url'] = girl_infor[i]
            girl['title'] = girl_title[i]
            girl['link'] = girl_link[i]
            # girl['big_imgs'] = None
            yield girl

        if response.meta.get('url') is not None:
            # 获取第一页中所有的页码
            page_url = response.xpath('//dd[@class="page"]/a/@href').extract()[-1]
            totle_page = int(page_url.split(".")[0].split("_")[-1])
            page_name = "_".join(page_url.split("_")[:-1])
            first_url = response.meta.get('url')
            for i in range(2,totle_page+1):
                yield scrapy.Request(url=("{0}/{1}_{2}.html".format(first_url,page_name,i)), callback=self.parse_model, meta={'model_name': response.meta['model_name']})
        # if response.meta.get('url') is not None:
        #     page_url = response.xpath('//dd[@class="page"]/a/@href').extract()[-1]
        #     totle_page = int(page_url.split(".")[0].split('_')[-1])
        #     page_name = "_".join(page_url.split("_")[:-1])
        #     first_url = response.meta.get('url')
        #     for url in range(2, totle_page):
        #         yield scrapy.Request(url=("{0}/{1}_{2}.html".format(first_url, page_name, i)),callback=self.parse_model, meta={'model_name': response.meta['model_name']})









