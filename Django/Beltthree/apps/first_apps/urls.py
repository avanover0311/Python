from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^(?P<id>\d+)/joinwish$', views.joinwish, name='joinwish'),
	url(r'^(?P<id>\d+)/addwish$', views.addwish, name='addwish'),
	url(r'^(?P<id>\d+)/viewwish$', views.viewwish, name='viewwish'),
	url(r'^(?P<id>\d+)/removewish$', views.removewish, name='removewish'),
	url(r'^createwish/$', views.createwish, name = 'createwish'),
	url(r'^logout/$', views.logout, name= 'logout'),
	url(r'^(?P<id>\d+)/display$', views.display, name= 'display'),
	url(r'^create/$', views.create, name='create'),
	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.index, name='index')
]