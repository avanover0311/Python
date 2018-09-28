from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)/deletetrip$', views.deletetrip, name='deletetrip'),
	url(r'^(?P<id>\d+)/jointrip$', views.jointrip, name='jointrip'),
	url(r'^(?P<id>\d+)/logout$', views.logout, name ='logout'),
	url(r'^addtrip/(?P<id>\d+)$', views.addtrip, name = 'addtrip'),
	url(r'^(?P<id>\d+)/createtrip$', views.createtrip, name='createtrip'),
	url(r'^(?P<id>\d+)/viewtrip$', views.viewtrip, name = 'viewtrip'),
	url(r'^(?P<id>\d+)/display$', views.display, name='display'),
	url(r'^create/$', views.create, name='create'),
	url(r'^login/$', views.login, name='login'),
	url(r'^$', views.index, name='index'),

]