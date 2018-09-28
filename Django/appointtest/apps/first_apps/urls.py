from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^(?P<id>\d+)/editappt$', views.editappt, name='editappt'),
	url(r'^(?P<id>\d+)/deleteappt$', views.deleteappt, name='deleteappt'),
	url(r'^(?P<id>\d+)/updateappt$', views.updateappt, name='updateappt'),
	url(r'^createapp/$', views.createapp, name = 'createapp'),
	url(r'^logout/$', views.logout, name= 'logout'),
	url(r'^(?P<id>\d+)/display$', views.display, name= 'display'),
	url(r'^create/$', views.create, name='create'),
	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.index, name='index')
]