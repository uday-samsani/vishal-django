from django.urls import path

from . import views as StudentView

urlpatterns=[
    path(r'student.profile/',StudentView.profile,name='profile'),
]