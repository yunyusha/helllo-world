from django.shortcuts import render
from django.conf import settings
# Create your views here.
def show_qq(requset):
    return render(requset, 'app3/qq.html')
