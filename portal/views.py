from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AlumniInfo
from .forms import AlumniInfoForm
from django.views.generic import ListView,DetailView
from django.db.models import Subquery
from .filters import AlumniInfoFilter

def index(request):
    count=AlumniInfo.objects.all().count()
    return render(request, template_name='index.html',context={'AlumniInfo':count})
    # using template index.html in portal/templates and context i.e. model info is passed out to views render

def thanks(request):
    return render(request,template_name='thanks.html',context={})


def submit_info(request):
    if request.method=='POST':
        form = AlumniInfoForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('thanks')
    else:
        form = AlumniInfoForm()
    return render(request,template_name= 'submit.html',context={'form':form})

'''
    class ListFeed(ListView):
        model = AlumniInfo
        paginate_by = 15
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
'''

def listfeed(request):
    search_term=''
    object_list=AlumniInfo.objects.all()
    if 'search' in request.GET:
        search_term=request.GET['search']
        object_list=AlumniInfo.objects.filter(name__icontains=search_term)
    return render(request, template_name='ListFeed.html', context={'object_list': object_list,'search_term':search_term})


def profile(request,id):

   record=AlumniInfo.objects.get(id=id)
   return render(request,template_name='profile.html',context={'record':record})