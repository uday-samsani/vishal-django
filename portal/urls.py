from django.urls import path
from . import views as portalView

urlpatterns=[
    path('',portalView.index,name='index'),
    path('submit/',portalView.submit_info,name='submit_info'),
]