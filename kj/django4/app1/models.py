from django.db import models
import mongoengine
# Create your models here.

class Accounts(mongoengine.Document):
    username = mongoengine.StringField(max_length=64,required=True,unique=True)
    password = mongoengine.StringField(max_length=64,required=True)


