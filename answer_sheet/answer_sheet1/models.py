from django.db import models
from mongoengine import *
connect('answer',host='127.0.0.1',port = 27017)
class Answer(Document):
    name = StringField()
    ans = StringField()