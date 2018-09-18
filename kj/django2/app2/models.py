from django.db import models
# from ..app1.models import Accounts
# Create your models here.
class Accounts(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
class Person(models.Model):
    nickname = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    photo = models.CharField(max_length=100)
    account = models.ForeignKey(Accounts,on_delete=True)