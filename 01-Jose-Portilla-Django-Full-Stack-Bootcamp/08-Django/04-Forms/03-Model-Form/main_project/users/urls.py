from django.urls import path
from users import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('all/', views.users, name='users'),
]

