from django.urls import path
from . import views as portalView

urlpatterns=[
    path('',portalView.index,name='index'),
    path('alumni/',portalView.submit_info,name='submit_info')
]