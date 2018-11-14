# -*- coding: utf-8 -*-
import scrapy,os,json
from ..items import Spider5Item

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['kaijiang.500.com']
    start_urls = ['http://kaijiang.500.com/shtml/ssq/']

    def __init__(self):
        path = os.path.abspath(os.path.dirname(__file__))
        self.file_path = os.path.join(path, 'num.json')
        self.numbers = []

        if os.path.exists(self.file_path):
            f = open(self.file_path, 'r')
            self.numbers = json.loads(f.read())
            f.close()

    # 实现爬虫第一次发送请求的操作
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'orFirst': True})


    def parse(self, response):
        # 获取所有的期数信息
        nums = response.xpath('//span[@class="iSelectBox"]/div/a/text()').extract()
        links = response.xpath('//span[@class="iSelectBox"]/div/a/@href').extract()

        # 开始发送请求,请求对应的双色球信息
        for i in range(len(nums)):
            if nums[i] not in self.numbers:

                yield scrapy.Request(url=links[i], callback=self.parse_ball, meta={'num':nums[i]})

    # 定义函数完成双色球信息的提取
    def parse_ball(self, response):
        # 获取期数信息
        # num = response.xpath("//font[@class='cfont2']/strong/text()").extract()[0]
        num = response.meta.get('num')
        self.numbers.append(num)
        # 获取红球和篮球信息
        ball_red = response.xpath('//li[@class="ball_red"]/text()').extract()
        ball_blue = response.xpath('//li[@class="ball_blue"]/text()').extract()[0]

        item = Spider5Item()
        item['number'] = num
        item['red'] = ball_red
        item['blue'] = ball_blue

        return item

    # 当爬虫因为某些原因被关闭时执行
    def close(spider, reason):
        print("++++++++++++++++++++++++")
        f = open(spider.file_path, 'w')
        f.write(json.dumps(spider.numbers))
