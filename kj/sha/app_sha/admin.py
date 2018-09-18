from django.contrib import admin

# Register your models here.
from .models import *
# 该文件是管理员文件,用来完成数据库数据模型的注册保证服务器端数据库和数据模型实现
# 数据的同步
admin.site.site_header = 'Appa'
admin.site.site_title = 'app1'
# 将Accounts数据模型注册进入数据库
admin.site.register(Accounts)
