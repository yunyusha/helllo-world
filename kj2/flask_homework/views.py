from flask import Flask,url_for, render_template,request
import os
from models import *

# 定义函数完成登录页面的渲染
def show_login():
    return render_template('login.html',css_path=url_for('static',filename='css/login.css'),url=url_for('account_login', _external=True),js_path=url_for('static', filename='js/jquery.min.js'))

# 定义函数完成注册页面的渲染
def show_regist():
    return render_template('regist.html', css_path=url_for('static',filename='css/login.css'),url=url_for('account_regist',_external=True),js_path=url_for('static', filename='js/jquery.min.js'))

# 定义函数完成注册功能的实现
def account_regist():
    if request.method == 'POST':
        username = request.values.get('user')
        password = request.values.get('passw')
        result = Regist.query.filter(Regist.r_id==username).first()
        if result is None:
            grade1 = Regist(username, password)
            db.session.add(grade1)
            db.session.commit()
            db.session.commit()
            msg = "注册成功"
        else:
            msg = "该账户已存在,请重试"
        return msg


# 添加功能完成登陆操作
def account_login():
    if request.method == 'POST':
        username = request.values.get('user')
        password = request.values.get('passw')
        result = Regist.query.filter(and_((Regist.r_id == username),Regist.r_password==password)).first()
        if result is not None:
            msg = "登录成功"
        else:
            msg = "密码或账号错误"
        return msg