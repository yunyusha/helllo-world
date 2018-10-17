from syst.views import render
from flask import url_for,request
from .models import *
import json
# 定义函数完成登录页面渲染
def show_login():
    dict = {
        'url':url_for('admin.static', _external=True,filename=''),
        'request_url':url_for('admin.login',_external=True),
    }
    return render('admin/login.html',**dict)


# 定义函数完成用户的登录操作
def login():
    if request.method == 'POST':
        # 获取用户名和密码
        account = request.values.get('account')
        passw = request.values.get('password')
        role = request.values.get('role')
        # 判断当当前登录是以手机号登录还是其他登录
        if len(account) == 11:
            if role == '老师':
                obj = Teacher.query.filter(Teacher.t_tel==account).first()
            else:
                obj = Student.query.filter(Student.s_tel==account).first()
        else:
            if role == '老师':
                obj = Teacher.query.filter(Teacher.t_id == account).first()
            else:
                obj = Student.query.filter(Student.s_id == account).first()

        if obj is not None:
            if hasattr(obj, 't_pass'):
                password = obj.t_pass
            else:
                password = obj.s_pass
            if password==passw:
                msg = {'code':200, 'account':account}
            else:
                msg = {'code':400, 'error':'密码不正确,重新输入'}
        else:
            msg = {'code':400, 'error': '用户不存在'}
        return json.dumps(msg)
