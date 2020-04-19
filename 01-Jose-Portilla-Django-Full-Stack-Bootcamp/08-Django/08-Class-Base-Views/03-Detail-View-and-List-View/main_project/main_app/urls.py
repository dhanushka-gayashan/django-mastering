from django.urls import path
from django.conf.urls import url
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
]

