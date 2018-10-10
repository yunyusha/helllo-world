from flask import Flask,url_for, render_template,request

# 定义函数完成登录页面的渲染
def show_login(request):
    return render_template('login.html',css_path=url_for('static',filename='css/login.css'))

# 定义函数完成注册页面的渲染
def show_regist(request):
    return render_template('regist.html', css_path=url_for('static',filename='css/login.css'))
