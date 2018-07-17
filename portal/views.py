from django.shortcuts import render
from django.http import HttpResponse
from .models import AlumniInfo
from .forms import AlumniInfoForm

def index(request):
    count=AlumniInfo.objects.all().count()
    return render(request, template_name='index.html',context={'AlumniInfo':count})
    # using template index.html in portal/templates and context i.e. model info is passed out to views render


def submit_info(request):
    form=AlumniInfoForm()
    return render(request,"submit.html",{'form':form})