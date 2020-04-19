from django.conf.urls import  url
from url_mapping import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]