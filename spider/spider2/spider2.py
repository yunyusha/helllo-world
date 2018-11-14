import urllib3,time,os
from multiprocessing import Pool,Manager
from lxml import etree
# 创建网络数据请求
http = urllib3.PoolManager()
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Content-type': 'text/json'}

# 定义函数完成网站数据的爬取
def get_net_data(url,method='get', callBack=None):
    response = http.request(method, url, headers=header, retries=5)
    if callBack is not None:
        callBack(response.data)
    else:
        return etree.HTML(response.data)

# 定义函数完成页面数据的下载
def download_page(d,model_name, url):
    dic = {}
    data = get_net_data(url)
    hrefs = data.xpath("//ul[@class='new-img']/ul/li/a/@href")
    srcs = data.xpath("//ul[@class='new-img']/ul/li/a/img/@src")
    titles = data.xpath("//ul[@class='new-img']/ul/li/a/@title")
    # 定义列表存储所有的图片数据
    min_len = min(len(hrefs), len(srcs), len(titles))
    imgs = []
    for i in range(min_len):
        dic = {'link':hrefs[i],'img_url':srcs[i],'title':titles[i]}
        imgs.append(dic)
        d[model_name] = imgs
        time.sleep(1)
    print("当前模块%s已经下载完毕" %(model_name))

# 定义函数创建二级文件夹
def make_dir(d):
    for key in dict(d):
        if not os.path.exists("images/{0}".format(key)):
            os.mkdir("images/{0}".format(key), 755)

# 定义函数完成三级目录的创建
def make_dir1(path,url):
    response = http.request('get', url, headers=header)
    if not os.path.exists(path):
        os.mkdir(path, 755)
    f = open('{0}/{1}'.format(path, url.split('-')[-1]),"wb+")
    f.write(response.data)
    f.close()
    time.sleep(1)
    print('%s 完成下载'%(url))

# 定义函数完成详情页面的数据抓取
def get_image_info(base_url, model_name, page_url, page_num,page_index,file_name=None):
    data = get_net_data(base_url+page_url)
    # 提取该页面的大图链接
    big_img = data.xpath('//div[@class="picsbox picsboxcenter"]/p/a/img/@src')
    make_dir1("images/{0}/{1}/img".format(model_name, page_num),big_img[0])
    # 判断下一页是否还有数据
    next_link = data.xpath('//div[@class="itempage"]/a/@href')[-1]
    if next_link != "#":
        print("即将下载下一页数据")
        time.sleep(1)
        get_image_info(base_url, model_name, "/{0}/{1}".format( model_name, next_link), page_num)
        return 0
    else:
        print("当前页面已经下载完成")
        return 0


if __name__ == '__main__':
    lists = [
        'http://www.7160.com/yulebagua/',
        'http://www.7160.com/meinvmingxing/',
        'http://www.7160.com/weimeitupian/',
        'http://www.7160.com/fengjing/',
        'http://www.7160.com/meishitupian/',
        'http://www.7160.com/qingchunmeinv/',
        'http://www.7160.com/xiaohua/',
        'http://www.7160.com/lianglichemo/'
    ]

    # 创建进程池
    pool1 = Pool(4)
    # 构建多进程通信需要的数据源
    d = Manager().dict()
    for url in lists:
        pool1.apply_async(download_page, args=(d, url.split('/')[-2],url))
    pool1.close()
    pool1.join()
    print(d)
    # 创建二级目录
    make_dir(d)

    # 创建三级目录
    pool2 = Pool(10)

    for key,value in dict(d).items():
        for i in range(1,len(value)+1):
            pool2.apply_async(make_dir1, args=('images/{0}/{1}'.format(key,i), value[i-1].get('img_url')))
    pool2.close()
    pool2.join()

    # 使用进程池完成图片详情页面的下载
    pool3 = Pool(8)
    for key,value in dict(d).items():
        for i in range(len(value)):
            pool3.apply_async(get_image_info, args=('http://www.7160.com',key,value[i].get('link'), (i+1)))
    pool3.close()
    pool3.join()

















