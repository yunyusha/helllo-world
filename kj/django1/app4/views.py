from django.shortcuts import render
from .models import *
# Create your views here.
def user(request):
    users = User.objects.all()
    return render(request, 'home.html',{'data':users})