from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .models import AlumniInfo
from .forms import AlumniInfoForm,UserCreationForm
from django.views.generic import ListView,DetailView
from django.db.models import Subquery
from .filters import AlumniInfoFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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

def login(request):
    logout(request)
    name=""
    password=""
    if request.POST:
        username=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                login(request)
                return redirect("/profile/")
    return render(request,template_name='login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,username)
            return redirect('/profile/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})