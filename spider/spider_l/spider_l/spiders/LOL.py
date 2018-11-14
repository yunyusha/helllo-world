# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import Hero
"""
SplashRequest: 专门用来生成基于splash加载的网络请求
"""
from scrapy_splash import SplashRequest



"""
script1: LUA语法脚本
  set_viewport_size(w, h): 用来设置浏览器页面的宽高;
  go(): 完成指定页面的加载;
    参数: url, baseurl, headers, http_method, body, formdata
      url: 需要加载的页面的网址;
      baseurl: 可选参数,默认为空,表示资源加载的相对路径;
      headers: 可选参数,默认为空,用来设置请求的header;
      http_method: 可选参数,默认为get,如果是post此时需要设置;
      body: 可选参数,默认为空,发送POST请求时向服务器传输的参数数据;
      formdata: 可选参数,默认为空,POST请求时的对应的表单数据,
      默认使用form表单默认的编码格式即application/x-www-form-urlencode.
  wait(): 用来等待网页的加载,单位为秒;
    参数: time, cancle_on_redirect, cancel_on_error 
      time: 延时时间;
      cancel_on_redirect: 可选参数,默认为false,用来设置当网页发生重定向时是否结束等待;
      cancel_on_error: 可选参数,默认为false,用来设置当网页发生错误时是否结束等待
  png(): 将加载之后的网站截屏,以png格式返回, 还有jpeg();
  html(): 将加载之后的网站以HTML格式返回
  
  jsfunc(): 将自定的javascript方法转化成LUA方法,但是自定义方法必须包含在[[]]中
  autoload(): 完成第三方资源远程链接,比如引入Jquery
"""
# 定义一段LUA脚本,控制页面行为
script1 = """
    function main(splash, args)
        splash:set_viewport_size(1200, 2000)
        splash.images_enabled = false
        splash:autoload('https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js')
        splash:go(args.url)
        splash:wait(args.wait)
        click_fun = splash:jsfunc([[
            function(){
                $('label[data-id="Tank"]').click();
            } 
        ]])
        click_fun()
        splash:wait(args.wait)
        return splash:png()
    end
"""

"""
返回字典类型数据时需要使用lxml的etree解析
"""
script2 = """
    function main(splash, args)
        splash:set_viewport_size(1200, 2000)
        splash:go(args.url)
        splash:wait(args.wait)
        return {'msg'='aa', data=splash.html()}
    end
"""

script3 = """
    function main(splash, args)
        splash:set_viewport_size(1200, 2000)
        splash.images_enabled = false
        splash:go("https://lol.qq.com/data/info-defail.shtml?id=Aatrox")
        splash:wait(args.wait)
        return splash:png()
    end
"""


class LolSpider(scrapy.Spider):
    name = 'LOL'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/data/info-heros.shtml']

    def start_requests(self):
        for url in self.start_urls:
            """
            endpoint: 设置splash渲染的方式,默认是render
            render: 只返回js渲染之后的网页,无法运行lua脚本;
            execute: 网页加载完成后还可以使用js操作,可以保证JS和LUA脚本的无缝融合
            args: 用来设置未来向LUA脚本中传递的参数,
                wait: 页面加载过程中等待的时间,单位为秒;
                lua_source: 需要执行的LUA脚本;
                url: 默认依据前面的url参数
            """
            yield SplashRequest(url=url, callback=self.parse,
                                endpoint='execute', args={'lua_source': script3, 'wait': 3})

    def parse(self, response):
        file = open('lol.png', 'wb+')
        file.write(response.body)
        file.close()
        # title = response.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@title').extract()
        # print(''.center(50, '+'))
        # print(title)
        # print(''.center(50, '-'))



