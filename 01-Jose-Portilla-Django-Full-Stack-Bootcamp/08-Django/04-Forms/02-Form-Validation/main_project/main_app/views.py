from django.shortcuts import render


# Create your views here.
from main_app import forms


def index(request):
    return render(request, 'main_app/index.html')


def form_view(request):
    form = forms.BasicForm()

    if request.method == 'POST':
        form = forms.BasicForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    context = {'form': form}
    return render(request, 'main_app/form.html', context=context)

