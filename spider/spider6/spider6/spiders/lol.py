# -*- coding: utf-8 -*-
import scrapy,os,json
from ..items import Hero
# 专门用来生成基于Splash加载的网络请求
from scrapy_splash import SplashRequest
from lxml import etree
# 定义一段lua脚本控制页面行为
script1 = """
    function main(splash, args)
        splash:set_viewport_size(1200,1200) --用来设置浏览器窗口的尺寸,w代表宽度,h代表高度
        
        splash:autoload('https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js')
        splash.images_enabled = false
        splash:go(args.url)
        splash:wait(args.wait) -- wait(time,cancle_on_redirect,cancel_on_error)
      
        click_fun = splash:jsfunc([[
            function(){
                var texts = $('label[data-id="Assassin"]').click();
            }
        ]])
        click_fun()
        splash:wait(args.wait)
        return splash:png()
        -- go(url, baseurl, headers, http_method, body,formdata):完成指定页面的加载
        -- url: 需要加载的页面的网址,baseurl :可选参数,默认为空,表示资源加载的相对路径
        -- headers: 可选参数,默认为空,用来设置请求的header
        -- http_method: 可选参数, 默认为空, 发送POST请求时向服务器传输的参数数据
        -- formdata: 可选参数,默认为空,POST的时候对应的表单数据,
        -- 默认使用form表单默认的编码格式即application/x-www-form-urlencode
        -- 延迟,用来等待网页的加载,对应的时间以秒为单位
        -- time: 等到网页加载的时间,以秒为单位
        -- cancle_on_redirect:可选参数,默认为false,用来设置当网页发送重定向时是否结束等待
        -- cancle_on_error:可选参数,默认为false,用来设置当前网页发生错误时是否结束等待
         -- 将加载之后的网站截屏,并以png格式返回
        -- html():将加载之后的网站以html格式返回, jpeg格式返回
        -- jsfunc(): 将自定义的javascript方法转化成lua方法,但是自定义方法必须包含在[[]]中
        -- autoload(): 完成第三方资源远程链接加载
    end
"""


class LolSpider(scrapy.Spider):
    name = 'lol'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/data/info-heros.shtml']

    def start_requests(self):
        for url in self.start_urls:
            # endpoint: 设置splash渲染的方式,默认是render.html:即直接返回js渲染之后的网页,如果页面需要进行认为操作时,此时需要使用execute,execute可以保证js和lua脚本实现无缝融合
            # args 未来向lua脚本中传递的参数,默认有一个url,该url在未设置时指向发送请求的url, wait:页面加载过程中等待的时间,单位为秒
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source': script1, 'wait': 7})

    def parse(self, response):
        f = open(os.path.join(os.path.dirname(__file__),'aa.png'), 'wb+')
        f.write(response.body)
        f.close()
        # print(response.body)
