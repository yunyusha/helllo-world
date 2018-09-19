from django.contrib import admin
from django.urls import path
from app3 import views

urlpatterns = [
    path('show_qq/', views.show_qq, name="qq"),
]
