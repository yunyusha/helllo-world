from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import time,json,os
from django.conf import settings
# Create your views here.
def render_upload(request):
    return render(request, 'app2/upload.html')

# 为服务器添加文件处理的功能
@csrf_exempt
def deal_file(request):
    # 获取前端传输的文件对象
    file_obj = request.FILES.get('files')
    # 获取文件类型
    img_type = file_obj.name.split('.')[1]
    # 将文件中的数据大写全部转换成小写
    img_type = img_type.lower()
    if img_type in ['png', 'jpg', 'jpeg', 'gif']:
        # 将图片存储到指定的目录
        # 获取当前时间的时间戳
        timestr = str(time.time()).replace('.', '')
        # 获取程序需要写入的文件路径
        path = os.path.join(settings.BASE_DIR, 'app2/file/img/{0}{1}'.format(timestr,file_obj.name))
        # 根据路径打开指定的文件(以二进制读写方式打开)
        f = open(path, 'wb')
        # 将对应的文件数据转换成若干片段,分段写入,可以有效提高文件的写入速度,适用于2.5M以上的文件
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        msg = {"code": 200, 'url': 'http://127.0.0.1:8000/app2/pass_data/{0}{1}'.format(timestr,file_obj.name), 'error': ''}

    else:
        # 存储失败,返回错误信息
        msg = {'code': 305, 'url': '','error': "文件类型不匹配"}
    return HttpResponse(json.dumps(msg))

# 定义函数完成指定服务器向前端返回指定文件
def pass_img_data(request,img_name):
    path = os.path.join(settings.BASE_DIR, 'app2/file/img/{0}'.format(img_name))
    if os.path.exists(path):
        # 文件存在,读取文件数据
        f = open(path, 'rb+')
        data = f.read()
        f.close()
        return HttpResponse(data)
    else:
        return HttpResponse('')

