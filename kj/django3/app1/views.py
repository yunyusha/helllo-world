from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse
import json
# Create your views here.
def show_major(request):
    return render(request,'major.html')

# 定义函数完成课程数据的接收
@csrf_exempt
def save_major(request):
    m_id = request.POST.get('m_id')
    m_name = request.POST.get('m_name')
    t_id = [int(i) for i in (request.POST.get('m_tea')).split(',')]

    # 从Teacher表中查找满足条件的教师信息
    # __in:查询指定的字段在某一个list中
    res = Teacher.objects.filter(card_id__in=t_id)
    # 从课程表中查找该课程是否存在,如果不存在,此时插入该课程
    res1 = Major.objects.filter(major_id=m_id)
    obj = None
    for item in res1:
        obj = item
    if obj is not None:
        # 课程存在,不能插入
        msg = {'code': 400, 'error': '课程信息存在,不能重复录入'}
    else:
        # 课程不存在,此时完成数据插入
        # 数据库表格中多对多字段进行数据录入时需要和普通字段(一对多字段,一对一字段和其他字段)分开进行数据录入
        # 先录入Major普通数据,并且获取录入的major对象
        major = Major(major_id=m_id, name=m_name)
        # 将数据保存到数据库
        major.save()
        # 向当前表格录入多对多数据字段
        major.t_id.set(res) # set为设置
        # 再次调用save将本次绑定的数据写入的数据库
        major.save()
        msg = {'code': 200, 'error': '', 'success': '数据录入成功'}
    return HttpResponse(json.dumps(msg))

# 定义函数完成对课程信息的更新
@csrf_exempt
def update_major_infor(request):
    m_id = request.POST.get('m_id')
    m_name = request.POST.get('m_name')
    t_id = request.POST.get('m_tea').split(',')
    # 根据传输的t_id获取对应的教师信息
    res = Teacher.objects.filter(card_id__in=t_id)
    # 查询课程id对应的课程信息
    res1 = Major.objects.filter(major_id=m_id)
    obj = None
    for item in res1:
        obj = item
    if obj is None:
        msg = {'code': 400, 'error': '查无此课程'}
    else:
        obj.name = m_name
        obj.t_id.set(res)
        obj.save()
        msg = {'code': 200, 'error': '', 'success': '数据更新成功'}
    return HttpResponse(json.dumps(msg))

# 添加函数完成对应课程的删除
@csrf_exempt
def delete_major(request):
    m_id = request.POST.get('m_id')
    res = Major.objects.filter(major_id=m_id)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        msg = {'code': 400, 'error': '不存在该课程'}
    else:
        obj.delete()
        msg = {'code': 200, 'error': '', 'success': '数据删除成功'}
    return HttpResponse(json.dumps(msg))

# 定义函数完成数据的查询操作
@csrf_exempt
def select_all(request):
    m_id = request.POST.get('m_id')
    res = Major.objects.filter(major_id=m_id)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        msg = {'code': 400, 'error': '该课程不存在'}
    else:
        # 查询教授该门课程的所有老师名字
        names = []
        for item in obj.t_id.all():
            names.append(item.name)
        dic = {'id': obj.major_id, 'mname': obj.name, 'tea_name': names}
        msg = {'code': 200, 'error': '', 'success': dic}
    return HttpResponse(json.dumps(msg))