from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'text': 'hello world',
        'number': 1000,
    }
    return render(request, 'main_app/index.html', context=context)


def other(request):
    return render(request, 'main_app/other.html')


def relative(request):
    return render(request, 'main_app/relative_url_templates.html')