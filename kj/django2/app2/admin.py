from django.contrib import admin
from .models import Person
# Register your models here.
admin.site.set_header = 'App2'
admin.site.set_titile = 'app2'
admin.site.register(Person)

