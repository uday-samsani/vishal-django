from django.urls import path
from . import views as portalView

urlpatterns=[
    path('',portalView.index,name='index')
]