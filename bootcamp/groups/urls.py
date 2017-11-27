from django.conf.urls import url

from bootcamp.groups import views

urlpatterns = [

    url(r'^$', views.groups, name='groups')

]

