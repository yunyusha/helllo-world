# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from .lua_js import *


script1 = """
    function main(splash, args)
        splash:set_viewport_size(1200,1200)
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash:go(args.url)
        splash:wait(args.wait)
        splash:wait(args.wait)
        return splash:html()
    end
    
    

"""
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source':script1,'wait': 5})

    def parse(self, response):
        path = response.xpath("//img[@class='lazyimg_img']/@src").extract()
        print("+++++++++++++")
        print(path)
        print("+++++++++++++")


