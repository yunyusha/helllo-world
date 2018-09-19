"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconffssa
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('upload/', views.render_upload, name="upload"),
    path('deal_file/<str:account>/', views.deal_file, name="deal_file"),
    path('pass_data/<str:account>/<str:img_name>/', views.pass_img_data,name='pass_data'),
    path('save_user_infor/', views.save_user_infor, name='save_user'),
    path('home/', views.render_home, name='home'),
    path('pass_user', views.pass_user_infor, name="pass_user"),
]
