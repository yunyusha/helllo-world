from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# viems.py主要完成服务器功能的开发,该文件通过不同的函数设置服务器不同的子功能
# HTTPResponse: 服务器基于HTTP协议的网络回应对象,该对象可以完成服务器向浏览器传输数据的
# request: 所有扩展服务器功能的函数都必须携带的参数,该参数用来存储浏览器向
# 服务器发送的数据请求的对象

# user,passsword:分别用来接收浏览器通过地址方式传输的数据,即数据作为网址的
# 组成部分被传输过来, 注意:不管网址中传输的数据是否是字符串,服务器接收到的
# 永远只有字符串数据
def welcome(request, user, password):
    return HttpResponse("欢迎蓝鸥!<br>你本次登录的用户名{0},密码是{1}".format(user, password))

# 定义函数完成指定页面的渲染
def show_login(request):
    return render(request, 'app1/login.html')

# 服务器接收浏览器通过GET或POST发送的数据
# request: 浏览器向服务器发送的网络请求对象,其中存储本次请求的各种信息
# 比如前端向服务器发送的数据参数,请求方式,网址等信息

# @csrf_exempt: 为服务器添加一个CSRF验证机制,保证服务器不会受到恶意攻击,该操作一般应用于POST请求中
@csrf_exempt
def receive_data(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return HttpResponse('您本次登录使用的用户名为{0},密码为{1}'.format(username, password))

# 定义函数完成show.html页面的渲染
def show(request):
    pers = [
        {'name': '冰哥', 'sex': '女', 'age': 20},
        {'name': '李坤', 'sex': '女', 'age': 38},
        {'name': '张引', 'sex': '男', 'age': 25},
        {'name': '刘乾', 'sex': '男', 'age': 40},
        {'name': '李炳辉', 'sex': '男', 'age': 35},
        {'name': '王凡', 'sex': '男', 'age': 18},
        {'name': '雨轩', 'sex': '女', 'age': 25},

    ]
    return render(request, 'app1/show.html', {'persons': pers})
