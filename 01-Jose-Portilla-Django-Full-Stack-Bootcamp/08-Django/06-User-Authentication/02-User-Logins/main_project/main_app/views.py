from django.shortcuts import render
from main_app.forms import UserForm, UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


def register(request):
    registered = False

    if request.method == "POST":
        # Mapping Form Data into Form Objects
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            user = user_form.save()

            # Hashing Password by calling 'set_password'
            user.set_password(user.password)

            # Save changers
            user.save()

            # Set Default User Object into the Profile Object
            # commit=False to avoid issues like insert duplicate records
            profile = profile_form.save(commit=False)
            profile.user = user

            # Set Profile Image File (Any kind of file)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            # Save Profile
            profile.save()

            # Change Status of Registration if all went good
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        # Create Form Objects
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # Set Context Object
    context = {
        "registered": registered,
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(request, 'main_app/registration.html', context=context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('INVALID LOGIN DETAILS SUPPLIED!')
    else:
        return render(request, 'main_app/login.html', {})


# Only logged-in users can logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Only logged-in users can access this
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

