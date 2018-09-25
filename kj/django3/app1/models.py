from django.db import models


# Create your models here.
class Teacher(models.Model):
    card_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    t_id = models.ManyToManyField(Teacher)

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    classroom = models.CharField(max_length=100)
    major_id = models.ManyToManyField(Major)
