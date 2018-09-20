from django.contrib import admin
from .models import Teacher, Student, Major
# Register your models here.
admin.site.set_header = 'App1'
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Major)
