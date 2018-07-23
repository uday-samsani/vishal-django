from django.urls import path
from . import views as portalView

urlpatterns=[
    path('',portalView.index,name='index'),
    path('submit/',portalView.submit_info,name='submit_info'),
    path('thanks/',portalView.thanks,name='thanks'),
    path('ListFeed/',portalView.ListFeed.as_view(template_name='ListFeed.html'),name='list-feed'),
    path(r'profile/(?P<id>\d+).$',portalView.profile,name='profile'),
    path(r'search/', portalView.search, name='search'),
    path(r'listfeed/',portalView.listfeed,name='listfeed'),

]