from django.db import models

# Create your models here.
# 用来创建Mysql数据库表格对应的数据模型.该模型相当于数据的载体用来完成开发
# 人员对表格数据的增删改查操作
# 注意每一个数据库模型对应的都是数据库中一张表格
class Accounts(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)

