# -*- coding: utf-8 -*-
import scrapy
from ..items import BeautifulGirl

class Spider1Spider(scrapy.Spider):
    # 设置爬虫的名字,用于区分不同爬虫
    name = 'spider1'
    # 设置当前爬虫爬取的网络链接
    allowed_domains = ['www.mm131.com']
    # 完成爬虫初始下载页的链接设置
    start_urls = ['http://www.mm131.com/']

    # 当网页下载完成后,需要执行回调函数,主要完成王网页数据的解析
    def parse(self, response): # response: 下载模块的下载数据, extract():将查找后的结果对象中的数据过滤
        urls = response.xpath("//div[@class='nav']/ul/li/a/@href").extract()[1:]
        model_names = response.xpath("//div[@class='nav']/ul/li/a/text()").extract()[1:]

        for i in range(len(urls)):
            # 生成新的数据请求对象
            yield scrapy.Request(url=urls[i], meta={'model_name': model_names[i], 'url': urls[i]},callback=self.parse_model)

    def parse_model(self, response):
        # 获取图片和标题
        girl_url = response.xpath("//div[@class='main']/dl/dd/a/img/@src").extract()
        girl_tit = response.xpath("//div[@class='main']/dl/dd/a/img/@alt").extract()
        # 获取图片详情页的链接
        girl_link = response.xpath("//div[@class='main']/dl/dd/a/@href").extract()
        length = min(len(girl_link), len(girl_tit), len(girl_url))
        print('++++++++++++++++')
        print(girl_url)
        print(girl_tit)
        print(girl_link)
        print('++++++++++++++++++')


        # 将数据构建成BeatifulGirl实例
        for i in range(length):
            girl = BeautifulGirl()
            girl['model_name'] = response.meta['model_name']
            girl['img_url'] = girl_url[i]
            girl['title'] = girl_tit[i]
            girl['link'] = girl_link[i]
            yield girl

        # 获取第一页所有的页码
        if response.meta.get('url') is not None:
            page_url = response.xpath('//dd[@class="page"]/a/@href').extract()[-1]
            totle_page = int(page_url.split(".")[0].split('_')[-1])
            page_name = "_".join(page_url.split("_")[:-1])
            first_url = response.meta.get('url')
            for i in range(2,totle_page+1):
                yield scrapy.Request(url=("{0}{1}_{2}.html".format(first_url, page_name, i)),callback=self.parse_model, meta={'model_name':response.meta['model_name']})

