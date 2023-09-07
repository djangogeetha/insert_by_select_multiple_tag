from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)   
    return render(request,'insert_webpage.html',d)

def insert_AccessRecord(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        pk=request.POST['pk']
        na=request.POST['na']
        aa=request.POST['author']
        da=request.POST['date']
        ur=request.POST['url']
        em=request.POST['email']
        TO=Topic.objects.get(topic_name=na)
        AC=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        AC.save()
        QSWO=Webpage.objects.all()
        d1={'QSWO':QSWO}
        return render(request,'display_AccessRecord.html',d1)   
    return render(request,'insert_AccessRecord.html',d)



def select_and_display(request):
    WTO=Topic.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        QSWO=Webpage.objects.none()
        for tn in tnlist:
            QSWO=QSWO|Webpage.objects.filter(topic_name=tn)

        d1={'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_and_display.html',d)   

def checkbox(request):
    WTO=Topic.objects.all()
    d={'WTO':WTO}

    return render(request,'checkbox.html',d)

def radiobutton(request):
    WTO=Topic.objects.all()
    d={'WTO':WTO}

    return render(request,'radiobutton.html',d)
