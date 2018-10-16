from flask import Flask,url_for, render_template,request
from views import *
from app import path
app = Flask(__name__)

# 该函数是路由装饰器@app.route()的底层实现方式,该方法可以实现指定
# 函数与对应路由的绑定操作
urls = ([
    path('/login/', show_login),
    path('/regist/', show_regist),
    path('/regist/account_regist/', account_regist),
    path('/account_login/', account_login),
])