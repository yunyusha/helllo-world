from django.db import models
from app1.models import Accounts
# Create your models here.
class Person(models.Model):
    nickname = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    photo = models.CharField(max_length=100)
    # 将Person表格中account字段和Acocunts模块进行关联,即account字段为Person模块的外键(一对多关系)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)

