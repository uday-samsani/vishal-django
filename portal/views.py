from django.shortcuts import render
from .models import AlumniInfo

def index(request):
    return render(request, template_name=index.html,context={'AlumniInfo':AlumniInfo.objects.all()})
    # using template index.html in portal/templates and context i.e. model info is passed out to views render