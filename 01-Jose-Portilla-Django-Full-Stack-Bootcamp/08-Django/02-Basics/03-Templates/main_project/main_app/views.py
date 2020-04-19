from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {"insert_me": "Hello, Welcome to Django World"}
    return render(request, 'main_app/index.html', context=data)



