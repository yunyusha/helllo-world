from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import time, json, os
from django.conf import settings
from .models import Person
from app1.models import Accounts
# Create your views here.
def render_upload(request):
    return render(request, 'app2/upload.html')

# 定义函数完成主页面渲染
def render_home(request):
    return render(request, 'app2/home.html')

# 为服务器添加文件处理的功能
@csrf_exempt
def deal_file(request, account):
    # 在制定的文件夹下面创建属于某一个账号的文件夹
    path1 = os.path.join(settings.BASE_DIR, 'app2/file/img/{0}'.format(account))
    if not os.path.exists(path1):
        os.mkdir(path1)
    else:
        for filename in os.listdir(path1):
            os.remove(os.path.join(path1, filename))
    # 获取前端传输的文件对象
    file_obj = request.FILES.get('files')
    # 获取文件类型
    img_type = file_obj.name.split('.')[1]
    # 将文件中的数据大写全部转换成小写
    img_type = img_type.lower()
    if img_type in ['png', 'jpg', 'jpeg', 'gif']:
        # 将图片存储到指定的目录
        # 获取当前时间的时间戳
        timestr = str(time.time()).replace('.', '')
        # 获取程序需要写入的文件路径
        path = os.path.join(settings.BASE_DIR, 'app2/file/img/{0}/{1}{2}'.format(account, timestr, file_obj.name))
        # 根据路径打开指定的文件(以二进制读写方式打开)
        f = open(path, 'wb')
        # 将对应的文件数据转换成若干片段,分段写入,可以有效提高文件的写入速度,适用于2.5M以上的文件
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        msg = {"code": 200, 'url': 'http://127.0.0.1:8000/app2/pass_data/{0}/{1}{2}'.format(account, timestr,file_obj.name), 'error': ''}

    else:
        # 存储失败,返回错误信息
        msg = {'code': 305, 'url': '','error': "文件类型不匹配"}
    return HttpResponse(json.dumps(msg))

# 定义函数完成指定服务器向前端返回指定文件
def pass_img_data(request,account,img_name):
    path = os.path.join(settings.BASE_DIR, 'app2/file/img/{0}/{1}'.format(account, img_name))
    if os.path.exists(path):
        # 文件存在,读取文件数据
        f = open(path, 'rb+')
        data = f.read()
        f.close()
        return HttpResponse(data)
    else:
        return HttpResponse('')

# 为服务器添加功能完成用户的基本信息的保存
@csrf_exempt
def save_user_infor(request):
    account = request.POST.get('account')
    nickname = request.POST.get('nickname')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    photo = request.POST.get('photo')
    # 查询当前表格中是否存在该用户信息
    account_name = account
    # 在jango中如果数据库表格中存在外键,此时外键存储的数据必须是一个与外键相关的数据模型对象,比如account字段作为Person模块的外键,该外键与Accounts模块关联,此时Accounts中存储的必须是一个Accounts类型的对象
    account = Accounts.objects.get(username=account)
    # 在django中如果需要通过外键访问所在表格中的数据时,需要通过"_"该符号进行访问
    res = Person.objects.filter(account__username=account_name)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        # 将该用户信息插入数据库
        Person.objects.create(account=account, nickname=nickname, sex=sex, age=age, photo=photo)
    else:
        Person.objects.update(account=account, nickname=nickname, sex=sex, age=age, photo=photo)

    msg = {'code': 200, 'msg': '数据保存成功'}
    return HttpResponse(json.dumps(msg))

# 定义函数完成服务器对指定用户资料的传送
@csrf_exempt
def pass_user_infor(request):
    account = request.POST.get('account')
    res = Person.objects.filter(account__username=account)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        msg = {'code': 203, 'infor':""}
    else:
        dic = {'nickname': obj.nickname, 'sex': obj.sex, 'age': obj.age, 'photo': obj.photo}
        msg = {'code': 200, 'infor': dic}

    return HttpResponse(json.dumps(msg))
