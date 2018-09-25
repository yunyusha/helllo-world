from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Accounts
import json,os,time
# Create your views here.
def show_st(request):
    return render(request, 'app1/st.html')

# 完成登录页面的渲染
def show_login(request):
    return render(request, 'app1/login.html')

# 完成注册页面的渲染
def show_regist(request):
    return render(request, 'app1/regist.html')

# 完成信息完善页面渲染
def render_upload(request):
    return render(request, 'app1/upload.html')

# 定义函数完成登录操作
@csrf_exempt
def login_data(request):
    username = request.POST.get('user')
    password = request.POST.get('passw')
    #查找用户名和密码
    result = Accounts.objects.filter(username=username)
    obj = None
    for item in result:
        obj = item

    if obj is None:
        msg = {'code': 300, 'error': '用户名不存在'}
    else:
        if obj.password == password:
            msg = {'code': 200, 'error':''}
        else:
            msg = {'code': 400, 'error': '密码错误'}
    return HttpResponse(json.dumps(msg))

# 完成服务器数据注册功能
@csrf_exempt
def regist_account(request):
    # 获取用户传入的账号和密码
    username = request.POST.get('user')
    password = request.POST.get('passw')
    # 查询数据库中是否含有该用户
    result = Accounts.objects.filter(username=username)
    obj = None

    for item in result:
        obj = item
    if obj is None:
        Accounts.objects.create(username=username, password=password)
        msg = {'code': 200, 'error': ''}
    else:
        msg = {'code': 400, 'error': '用户名已存在'}
    return HttpResponse(json.dumps(msg))

# 为服务器添加文件处理功能
@csrf_exempt
def deal_file(request,account):
    # 在指定的文件夹下面创建属于某一个账号的文件夹
    path1 = os.path.join(settings.BASE_DIR,'app1/file/img/{0}'.format(account))
    if not os.path.exists(path1):
        os.mkdir(path1)
    else:
        for filename in os.listdir(path1):
            os.remove(os.path.join(path1, filename))
    # 获取前端传输的文件对象
    file_obj = request.FILES.get('file')
    # 获取文件类型
    img_type = file_obj.name.split('.')[1]
    # 将文件类型中的数据大小写全部转换成小写
    img_type = img_type.lower()

    if img_type in ['png','jpg','jpeg','gif']:
        # 获取当前事件戳
        timestr = str(time.time()).replace('.', '')

        # 获取程序需要写入的文件路径
        path = os.path.join(settings.BASE_DIR,'app1/file/img/{0}/{1}{2}'.format(account,timestr,file_obj.name))

        # 根据路径打开制定的文件(以二进制读写方式打开)
        f = open(path, 'wb+')

        # chunks将对应的文件数据转换成若干片段,分段写入,可以有效提高文件的写入速度,适用于2.5M以上的文件
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        msg = {'code': 200, 'url': 'http://127.0.0.1:8000/app2/pass_data/{0}/{1}{2}'.format(account, timestr, file_obj.name),'error': ''}
    else:
        # 存储失败,返回错误信息
        msg = {'code': 302, 'url': '', 'error': '文件类型不匹配'}
    return HttpResponse(json.dumps(msg))

