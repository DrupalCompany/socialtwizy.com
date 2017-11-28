from . import views

from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.groups, name='groups'),
    url(r'^(?P<group_slug>[\w-]+)-(?P<group_id>\w+)/$', views.group, name='groups'),
    #url(r'group', views.group, name='group'),
]