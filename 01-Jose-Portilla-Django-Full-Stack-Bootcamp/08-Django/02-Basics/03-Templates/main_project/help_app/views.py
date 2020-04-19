from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    context = {'status': 'We are under construction'}
    return render(response, 'help_app/index.html', context=context)
