from django.shortcuts import render
from .models import AlumniInfo

def index(request):
    count=AlumniInfo.objects.all().count()
    return render(request, template_name='index.html',context={'AlumniInfo':count})
    # using template index.html in portal/templates and context i.e. model info is passed out to views render