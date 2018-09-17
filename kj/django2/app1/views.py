from django.shortcuts import render
from .models import Accounts
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 完成登录页面的渲染
def show_login(request):
    return render(request, 'app1/login.html')

# 完成注册页面的渲染
def show_regist(request):
    return render(request, 'app1/regist.html')

# 完成服务器的注册功能
@csrf_exempt
def regist_account(request):
    # 获取用户传输的账号和密码
    username = request.POST.get('user')
    password = request.POST.get('passw')
    # 查询数据库中是否含有该用户
    result = Accounts.objects.filter(username=username)

    # 首先获取表格中指定的数据,如果不存在则创建该数据
    # obj, result = Accounts.objects.get_or_create(dict)
    obj =None
    for item in result:
        obj = item
    if obj is None:
        Accounts.objects.create(username=username,password=password)
        msg = {'code': 200, 'error': ''}
    else:
        msg = {'code': 300, 'error': '用户名已存在'}
    return HttpResponse(json.dumps(msg))

# 定义一个函数完成登录操作
@csrf_exempt
def login_data(request):
    username = request.POST.get('user')
    password = request.POST.get('passw')

    # 查找用户名和密码
    result = Accounts.objects.filter(username=username)
    obj = None
    for item in result:
        obj = item
    if obj is None:
        msg = {'code': 300,'error': '用户名不存在'}
    else:
        if obj.password == password:
            msg = {'code': 200, 'error': ''}
        else:
            msg = {'code': 400, 'error': '密码错误'}
    return HttpResponse(json.dumps(msg))

