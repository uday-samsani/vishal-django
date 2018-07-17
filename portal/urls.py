from django.urls import path
from . import views as portalView

urlpatterns=[
    path('',portalView.index,name='index'),
    path('submit/',portalView.submit_info,name='submit_info'),
<<<<<<< HEAD
    path('thanks/',portalView.thanks,name='thanks'),
    path('ListFeed/',portalView.ListFeed.as_view(template_name='ListFeed.html'),name='list-feed'),
    path(r'profile/(?P<name>\d+).$',portalView.profile,name='profile')
    # path('ListDetailed',portalView.ListDetailed.as_view(template_name=''))
=======
>>>>>>> ae56f8457f903acf6de2ce784f04dd88528d439a
]