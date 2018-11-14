import urllib3
from PIL import Image
from pytesseract import image_to_string
import numpy
from lxml import etree
from PIL import Image,ImageFilter
import requests
from bs4 import BeautifulSoup
#import test2
# 创建http请求对象
http = urllib3.PoolManager()
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36', 'Content-type': 'text/json'}
res = http.request('get',"http://www.ztbu.edu.cn/captcha/1",headers=header)

# 将下载的验证码存储到指定路径
f = open('yz.png', 'wb+')
f.write(res.data)
f.close()

# def open_img(giffile):
#     img = Image.open(giffile)   #打开图片
#     img = img.convert('RGB')    #转换为RGB图
#     pixdata = img.load()        #转换为像素点图
#     return img, pixdata
# def remove_line(giffile, savepath):
#     (img, pixdata) = open_img(giffile)
#     for x in range(img.size[0]):    #x坐标
#         for y in range(img.size[1]):    #y坐标
#             if pixdata[x, y][0] < 8 or pixdata[x, y][1] < 6 or pixdata[x, y][2] < 8 or (
#                     pixdata[x, y][0] + pixdata[x, y][1] + pixdata[x, y][2]) <= 30:  #确定颜色阈值
#                 if y == 0:
#                     pixdata[x, y] = (255, 255, 255)
#                 if y > 0:
#                     if pixdata[x, y - 1][0] > 120 or pixdata[x, y - 1][1] > 136 or pixdata[x, y - 1][2] > 120:
#                         pixdata[x, y] = (255, 255, 255) #?
#
#     # 二值化处理
#     for y in range(img.size[1]):  # 二值化处理，这个阈值为R=95，G=95，B=95
#         for x in range(img.size[0]):
#             if pixdata[x, y][0] < 160 and pixdata[x, y][1] < 160 and pixdata[x, y][2] < 160:
#                 pixdata[x, y] = (0, 0, 0)
#             else:
#                 pixdata[x, y] = (255, 255, 255)
#     img.filter(ImageFilter.EDGE_ENHANCE_MORE)  #深度边缘增强滤波，会使得图像中边缘部分更加明显（阈值更大），相当于锐化滤波
#     img.resize(((img.size[0]) * 2, (img.size[1]) * 2), Image.BILINEAR)  # Image.BILINEAR指定采用双线性法对像素点插值#?
#     img.save(savepath+'captcha_removeline.gif')
# remove_line('H:\project\helllo-world\spider\spider3\yz.png','H:\project\helllo-world\spider\spider3\yz.png')


# 开始识别验证码中的数据
img = Image.open('yz.png')
# 图像灰度处理

# 获取图像所有的像素点
pix = img.load()
# 获取图像宽度和高度
w,h = img.size
for i in range(w):
    for j in range(h):
        val = (pix[i,j][0]+pix[i,j][1]+pix[i,j][2])//3
        pix[i,j] = (val, val, val)
img.save('yz1.png','png')

# 将经过灰度处理之后的图片进行二值化处理
img = Image.open('yz1.png')
pix = Image('yz1.png').load()
for i in range(h):
    for j in range(h):
        if pix[i, j][0] <=100:
            pix[i, j] = (0,0,0)
        else:
            pix[i, j] = (255,255,255)
img.save('yz2.png')

# 图片转成黑白图片
img.convert('L')
# 开始识别图片中的二维码
text = image_to_string(img, config='-psm 7')
print(text)

