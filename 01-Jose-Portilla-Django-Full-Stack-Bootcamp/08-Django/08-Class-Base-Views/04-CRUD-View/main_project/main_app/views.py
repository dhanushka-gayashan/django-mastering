from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from main_app import models


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    # ListView automatically create "school_list" object for context.
    # This "school_list" can be access from school_list.html without any additional coding
    # If you want to customize the name, you can use following approach
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    # DetailView automatically create "school" object for context.
    # This "school" can be access from school_detail.html without any additional coding
    # If you want to customize the name, you can use following approach
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'main_app/school_detail.html'


class SchoolCreateView(CreateView):
    # Only Editable Fields
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    # Only Editable Fields
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("main_app:list")

