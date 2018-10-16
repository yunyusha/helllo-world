from flask import Flask,url_for, render_template,request
import os

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
        base_dir = os.path.dirname(__file__) # 获取当前文件所在的文件路径
        path = os.path.join(base_dir, 'account') # 路径的拼接
        if not os.path.exists(path):
            os.mkdir(path, 755)
        # 将账号密码存储到指定的文件中
        if not os.path.exists(os.path.join(path,'account.txt')):
            f = open(os.path.join(path, 'account.txt'), 'a+')
        else:
            f = open(os.path.join(path,'account.txt'), 'r')
        txt = f.read()
        f.close()
        infors = txt.split(';')
        # 判断用户账号是否存在,刚开始假定不存在
        orexist = False
        for item in infors:
            if item.split('=')[0] == username:
                orexist = True
                break
        if orexist:
            f.close()
            return '用户名已存在,请重新输入!'
        else:
            f = open(os.path.join(path, 'account.txt'), 'a+')
            txt = '{0}={1};'.format(username, password)
            f.write(txt)
            f.close()
            return '恭喜你注册成功!'

# 添加功能完成登陆操作
def account_login():
    if request.method == 'POST':
        username = request.values.get('user')
        password = request.values.get('passw')
        base_dir = os.path.dirname(__file__)
        if os.path.exists(os.path.join(base_dir, 'account/account.txt')):
            f = open(os.path.join(base_dir, 'account/account.txt'), 'r')
            txt = f.read()
            f.close()
            infors = txt.split(';')
            # 记录用户输入的账号密码是否正确,默认不正确
            orright = False
            for item in infors:
                data = item.split('=')
                if data[0] == username and data[1] == password:
                    orright = True
                    break
            if orright:
                return '用户登录成功'
            else:
                return '用户名或密码不正确,请重新登录'
