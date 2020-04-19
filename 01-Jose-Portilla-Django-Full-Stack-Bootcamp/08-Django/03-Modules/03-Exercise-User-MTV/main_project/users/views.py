from django.shortcuts import render
from users.models import User


# Create your views here.
def index(request):
    users_list = User.objects.order_by('first_name')
    context = {"users_list": users_list}
    return render(request, 'users/index.html', context=context)

