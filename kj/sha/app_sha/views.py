from django.shortcuts import render
from .models import Accounts
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
# 登录页面的渲染
def show_login(request):
    return render(request, 'sha/login.html')
# 注册页面的渲染
def show_regist(request):
    return render(request, 'sha/regist.html')

# 完成服务器数据的注册功能
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
        Accounts.objects.create(username=username,password=password)
        msg = {'code': 200, 'error': ''}
    else:
        msg = {'code': 400, 'error': '用户名已存在'}
    return HttpResponse(json.dumps(msg))
