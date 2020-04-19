from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "func_index.html")


class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!!")


class TemplateCBView(TemplateView):
    template_name = 'tcbv_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!!'
        return context


