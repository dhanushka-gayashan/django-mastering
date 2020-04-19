from django.shortcuts import render

from users.forms import NewUserForm
from users.models import User


# Create your views here.
def index(request):
    context = {
        "title": "Welcome to user management center",
    }
    return render(request, 'users/index.html', context=context)


def users(request):
    users_list = User.objects.order_by('first_name')
    context = {
        "title": "Here are your users list:",
        "users_list": users_list,
    }
    return render(request, 'users/users.html', context=context)


def signup(request):
    form = NewUserForm

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'users/signup.html', context={
        'title': 'Please sign up here!',
        'form': form
    })
