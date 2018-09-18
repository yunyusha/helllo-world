from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'App1x'
admin.site.site_title = 'app1x'

# 将Accounts数据模型注册进入数据库
admin.site.register(Accounts)
