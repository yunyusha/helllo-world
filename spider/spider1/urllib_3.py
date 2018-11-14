"""

urllib3是一个功能强大,调理清晰,用于HTTP请求的Python库,许多Python的原生系统都已经开始使用urllib3,urllib3提供了Python标准库urllib中所没有的重要特性
1. 线程安全
2. 链接池
3. 客户端SSL/TLS验证
4. 文件分布编码上传
5. 协议处理重复请求和HTTP重定位
6. 支持压缩编码
7. 支持HTTP和SOCKS代理(IP的更换操作)

"""

import urllib3
# get请求
# 创建网络请求
http = urllib3.PoolManager()
# 发送网络请求
# response = http.request('get', 'http://www.baidu.com')
# 获取响应结果
# print(response.data.decode())
"""

request(method, url, fileds, headers): 用来完成指定链接的数据请求,其中:
method:设置请求方式,常用的请求方式GET,POST
url:设置请求的链接
fields设置对应请求需要发送的参数,该数据是字典类型,可以通过键值对设置
headers: 用来设置请求的头部信息, 比如设置数据的编码格式,数据的参数类型,
模拟浏览器发送请求等

"""
# 模拟浏览器发送请求
urllib3.disable_warnings() # 禁用urllib3警告(urllib3在进行https请求时会抛出对应的警告.可以设置disable_warnings)禁用对应的警告
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Content-type': 'text/json'}
# response = http.request('get', 'https://www.taobao.com',headers=header)
# print(response.data.decode())
# 进行IP代理
# 设置IP代理
# manage = urllib3.ProxyManager('http://192.168.17.134', headers=header)
# 调用代理对象,执行网络请求
# response = manage.request('get', 'http:www.baidu.com')
# print(response.data.decode())

response = http.request('get', 'http://www.aaa.com', retries=5)
print(response.retries)
print(response.data.decode())
