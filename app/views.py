from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
#from app.models import *
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse(f'Toic data is inserted')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WPO=WebpageForm()
    d={'WPO':WPO}
    if request.method=='POST':
        WO=WebpageForm(request.POST)
        if WO.is_valid():
            WO.save()
            return HttpResponse('Web page data is inserted')

    return render(request,'insert_webpage.html',d)


def insert_access(request):
    ARF=AccessRecordForm()
    d={'ARF':ARF}
    if request.method=='POST':
        AO=AccessRecordForm(request.POST)
        if AO.is_valid():
            AO.save()
            return HttpResponse('access data is inserted')
    return render(request,'insert_access.html',d)