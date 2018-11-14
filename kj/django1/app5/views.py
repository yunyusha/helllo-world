from django.shortcuts import render
from .models import *
# Create your views here.
def person(request):
    person_get = Person.objects.all()
    return render(request, 'person.html', {'data':person_get})


