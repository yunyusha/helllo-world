from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator
from answer_sheet1.models import Answer
import json,time
import os
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from answer_sheet1.get_answer import *

def test(request):
    return HttpResponse(json.dumps({'msg':'11111111'}))


# 为服务器添加处理文件的功能
@csrf_exempt
def deal_file(request):
    # 在指定的文件夹下面创建属于某一个账号的文件夹
    real = request.POST.get('data')
    res = Answer.objects.filter(name=real)
    for item in res:
        ans = item.ans
    ans = json.loads(ans)
    path1 = os.path.join(settings.BASE_DIR,'answer_sheet1/file/img')
    if not os.path.exists(path1):
        os.mkdir(path1)

    file_obj = request.FILES.get('file')
    # img_type = file_obj.name.split('.'[1])
    # 将文件类型中的数据大写全部转换成小写
    # img_type = img_type.lower()

        # 将图片存储在指定的目录
        # 获取当前时间的时间戳
    timestr = str(time.time()).replace('.','')
        # 获取程序需要写入的文件路径
    path = os.path.join(settings.BASE_DIR,'answer_sheet1/file/img/{0}{1}'.format(timestr,file_obj.name))
        # 根据路径打开指定的文件(以二进制读写方式打开)
    f = open(path,'wb+')
        # chunk将对应的文件数据转换成若干片段,分段写入,可以有效提高文件写入速度,适用于2.5M以上的文件
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()
    data = f_detail(path)
    answ = []
    for i in data:
        answ.append(judge(i))
    for te in range(len(answ)):
        answ[te][1+te*5]=answ[te][1]
        answ[te][2+te*5]=answ[te][2]
        answ[te][3+te*5]=answ[te][3]
        answ[te][4+te*5]=answ[te][4]
        answ[te][5+te*5]=answ[te][5]
        if te>0:
            answ[te].pop(1)
            answ[te].pop(2)
            answ[te].pop(3)
            answ[te].pop(4)
            answ[te].pop(5)

    answe = {**answ[0],**answ[1],**answ[2],**answ[3],**answ[4]}
    number = 0
    for key,values in answe.items():
        if ans[str(key)]==values:
            number=number+1
    msg = {'code': 200,'url':'127.0.0.1:8000/answer_sheet1/pass_data/{0}{1}'.format(timestr,file_obj.name),'answ':answ,'number':number}
    return HttpResponse(json.dumps(msg))

@csrf_exempt
def save(request):
    data = request.GET.get('data')
    real = json.loads(data)
    name = real['input']
    res = Answer.objects.filter(name=name)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        twz = Answer.objects.create(name=name,ans=data)
        twz.save()

    msg = {'code':200,'msg':'数据创建成功'}
    return HttpResponse(json.dumps(msg))

@csrf_exempt
def load(request):
    res = Answer.objects.all()
    name = []
    for item in res:
        name.append(item.name)
    msg = {'code':200,'name':name}
    return HttpResponse(json.dumps(msg))