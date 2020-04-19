from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'Welcome to Home Page'}
    return render(request, 'my_app/index.html', context=context)


