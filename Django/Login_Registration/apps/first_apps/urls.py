from django.conf.urls import url
from . import views

           
urlpatterns = [
	url(r'^viewtrip/$', views.viewtrip, name='viewtrip'),
	url(r'^addtrip/$', views.addtrips, name='addtrip'),
	url(r'^trips/$', views.trips, name='trips'), 
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.create),
	url(r'^$', views.index)
] 

