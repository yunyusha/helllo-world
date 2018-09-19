from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# 导入当前工程的settings.py文件
from django.conf import settings
from django.shortcuts import render
import os
import json

# Create your views here.
# 定义函数完成login页面的渲染
def show_login(request):
    return render(request, 'app2/login.html')

# 定义函数完成注册页面的渲染
def show_regist(request):
    return render(request, 'app2/regist.html')

# 定义函数完成服务器的注册功能
def regist(requset):
    user = requset.POST.get('user')
    password = requset.POST.get('passw')
    if deal_data(user, password) is True:
        return render(requset, 'app2/login.html')
    else:
        return HttpResponse('对不起本次注册失败')
# 定义函数完成服务器登录功能
def log_in(request):
    user = request.POST.get('user')
    password = request.POST.get('passw')
    if deal_logindata(user, password) is True:
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败')
# 定义函数完成登录数据处理
def deal_logindata(user,password):
    path = os.path.join(settings.BASE_DIR, 'app2/data/account.txt')
    if os.path.exists(path):
        # 文件存在
        f = open(path, 'r')
        data_list = json.loads(f.read())
        f.close()
        # 定义一个变量存储当前用户是否存在
        r = False
        for obj in data_list:
            if obj.get('user') == user and obj.get('pass') == password:
                r = True
                break
        if r is True:
            return True
        else:
            return False
    else:
        return False


# 定义函数完成数据处理
def deal_data(user, password):
    if len(user) == 0 or len(password) == 0:
        return False
    else:
        # 获取当前写入的数据的文件路径
        path = os.path.join(settings.BASE_DIR, 'app2/data/account.txt')
        if os.path.exists(path):
            # 文件存在
            f = open(path, 'r')
            data_list = json.loads(f.read())
            f.close()
            # 定义一个变量存储当前是否存在
            or_exist = False
            for obj in data_list:
                if obj.get('user') == user:
                    or_exist = True
                    break
            if or_exist is True:
                # 用户存在
                return False
            else:
                # 用户不存在
                data_list.append({'user': user, 'pass': password})
                f = open(path, 'w')
                f.write(json.dumps(data_list))
                f.close()
                return True
        else:
            # 文件不存在
            f = open(path, 'w')
            data = [{'user': user, 'pass': password}]
            f.write(json.dumps(data))
            f.close()
        return True

