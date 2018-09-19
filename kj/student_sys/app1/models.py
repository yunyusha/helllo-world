from django.db import models

# Create your models here.
class Accounts(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)

class Stu_msg(models.Model):
    username = models.ForeignKey(Accounts,on_delete=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField(max_length=3)
    sex = models.CharField(max_length=5)

