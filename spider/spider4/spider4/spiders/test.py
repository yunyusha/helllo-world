from urllib import request
import re
from bs4 import BeautifulSoup


def get_html(url):
    req = request.Request(url)
    return request.urlopen(req).read()


if __name__ == '__main__':
    url = "http://www.mm131.com/xinggan/list_6_2.html"
    html = get_html(url)
    data = BeautifulSoup(html, "lxml")
    p = r"(http://www\S*/\d{4}\.html)"
    get_list = re.findall(p, str(data))
    # 循化人物地址
    for i in range(20):
        # print(get_list[i])
        # 循环人物的N页图片
        for j in range(200):
            url2 = get_list[i][:-5] + "_" + str(j + 2) + ".html"
            try:
                html2 = get_html(url2)
            except:
                break
            p = r"(http://\S*/\d{4}\S*\.jpg)"
            get_list2 = re.findall(p, str(html2))
            print(get_list2[0])
        break