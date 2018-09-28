from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)/logout$', views.logout, name ='logout'),
	url(r'^(?P<id>\d+)/deletequote$', views.deletequote, name='deletequote'),
	url(r'^(?P<id>\d+)/addquote$', views.addquote, name = 'addquote'),
	url(r'^(?P<id>\d+)/editaccount$', views.editaccount, name = 'editaccount'),
	url(r'^(?P<id>\d+)/viewquotes$', views.viewquotes, name = 'viewquotes'),
	url(r'^(?P<id>\d+)/display$', views.display, name='display'),
	url(r'^create/$', views.create, name='create'),
	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.index, name='index'),
]