"""django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # 页面渲染
    path('show_major/', show_major,name='show_major'),
    path('show_stu/', show_stu, name='ss'),
    # 数据处理
    path('save_major/', save_major, name='sm'),
    path('updata_major', update_major_infor, name='um'),
    path('delete_major/', delete_major, name='dm'),
    path('select_major/', select_all, name='lm'),
    path('save_stu/', save_stu, name='ss'),

]
