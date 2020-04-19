from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'Sun Rise'}
    return render(request, 'main_app/index.html', context=context)
