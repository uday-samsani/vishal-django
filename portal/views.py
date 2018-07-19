from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AlumniInfo
from .forms import AlumniInfoForm
from django.views.generic import ListView,DetailView
from django.db.models import Subquery

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

class ListFeed(ListView):

    model = AlumniInfo
    paginate_by = 15  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

'''
class ListDetailed(DetailView):

    model = AlumniInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
'''
def profile(request,name1):

   record=AlumniInfo.objects.get(name=name1)
   return render(request,template_name='profile.html',context={'record':record})
   # return HttpResponse('Hi this is a profile of {}'.format(name))



