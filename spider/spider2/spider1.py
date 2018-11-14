import urllib3
import re
import time
from lxml import etree
from multiprocessing import Pool
import os

http = urllib3.PoolManager()

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Content-type': 'text/json'}

response = http.request('get', 'http://www.7160.com/', headers=header)
# datas = re.findall('<dl class="row2" id="tuijian">([a-zA-Z<>]*)</dl>',response.data)
# html = html.fromstring(response.data)
# print(html)
element = etree.HTML(response.data)
eles = element.xpath('//a[@class="addcss_a"]/img/@src|//a[@class="addcss_a"]/img/@title')
# print(eles)
# 定义函数完成图片数据的下载操作
def download(url, file_name, header):
    response = http.request('get', url, headers=header)
    os.mkdir('img/{0}'.format(file_name), 755)
    img_name = url.split("-")[-1]
    f = open('img/{0}/{1}'.format(file_name, img_name), "wb+")
    f.write(response.data)
    f.close()
    print("下载中")
    time.sleep(1)

if __name__ == "__main__":
    # eles = get_img_data(http)

    pool = Pool(5)
    for i in range(len(eles)):
        if i % 2 == 0:
            pool.apply_async(download, args=(eles[i], eles[i+1], header))
    pool.close()
    pool.join()
    print("下载任务结束")