from django.urls import path
from main_app import views

# TEMPLATE URLS
app_name = 'main_app'

urlpatterns = [
    path('register/', views.register, name='register')
]
