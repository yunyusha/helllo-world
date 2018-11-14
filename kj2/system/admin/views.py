from syst.views import render
from flask import url_for,request
from sqlalchemy import *
from .models import *
import json

# 定义函数完成登录页面渲染
def show_login():
    dict = {
        'url':url_for('admin.static', _external=True,filename=''),
        'request_url':url_for('admin.login',_external=True),
    }
    return render('admin/login.html',**dict)

# 定义函数完成添加页面的显示
def show_add():
    dict = {'url':url_for('admin.add_infor',_external=True)}
    return render('admin/add.html',**dict)

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
                if hasattr(obj, 't_pos'):
                    pos = obj.t_pos
                else:
                    pos = '学生'
                msg = {'code':200, 'account':account,'pos':pos, 'role':role}
            else:
                msg = {'code':400, 'error':'密码不正确,重新输入'}
        else:
            msg = {'code':400, 'error': '用户不存在'}
        return json.dumps(msg)

# 定义函数完成用户信息的添加
def add_infor():
    if request.method == 'POST':
        # 获取用户角色信息
        role = request.values.get('role')
        account = request.values.get('account')
        tel = request.values.get('tel')
        name = request.values.get('name')
        if role == '老师':
            obj = Teacher.query.filter(or_(Teacher.t_id==account,Teacher.t_tel==tel)).first()
            if obj is None:
                Teacher.add(t_id=account,t_pass=123,t_tel=tel,t_name=name)
                msg = {'code':200, 'msg': '添加成功'}
            else:
                msg = {'code': 400, 'msg': '添加失败'}
        else:
            sex = request.values.get('sex')
            obj = Student.query.filter(or_(Student.s_id == account, Student.s_tel == tel)).first()
            if obj is None:
                Student.add(s_id=account, s_pass=123, s_tel=tel, s_name=name, s_sex=sex)
                msg = {'code': 200, 'msg': '添加成功'}
            else:
                msg = {'code': 400, 'msg': '添加失败'}
        return json.dumps(msg)



