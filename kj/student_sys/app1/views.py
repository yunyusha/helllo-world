from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Accounts
import json
# Create your views here.
def show_st(request):
    return render(request, 'app1/st.html')

# 完成登录页面的渲染
def show_login(request):
    return render(request, 'app1/login.html')

# 完成注册页面的渲染
def show_regist(request):
    return render(request, 'app1/regist.html')

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

