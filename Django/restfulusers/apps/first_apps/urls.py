from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)/updateuser$', views.updateuser, name='updateuser'),
	url(r'^(?P<id>\d+)/deleteuser$', views.deleteuser, name='deleteuser'),
	url(r'^(?P<id>\d+)/edituser$', views.edituser, name='edituser'),
	url(r'^(?P<id>\d+)/viewuser$', views.display, name ='viewuser'),
	url(r'^adduser/create/$', views.create),
	url(r'^adduser/$', views.adduser, name = 'adduser'),
	url(r'^$', views.index, name ='index')
]