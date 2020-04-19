from django.shortcuts import render
from my_app.models import Topic, Webpage, AccessRecord


# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    context = {'access_records': webpage_list}
    return render(request, 'my_app/index.html', context=context)


