from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')
	
def create(request):
	 if User.objects.registration_validator(request.POST, request):
	 	passFlag=True
	 	user = User.objects.get(email=request.POST['email'])
	 	return redirect(reverse('display',kwargs={'id': user.id }))
	 else:
	 	return redirect(reverse('index'))

def login(request):
	
	if User.objects.login_validator(request.POST, request):
		passFlag = True
		user = User.objects.get(email=request.POST['email_login'])
		request.session['id']=user.id
		return redirect(reverse('display',kwargs={'id': user.id }))
	else:
		return redirect(reverse('index'))

def display(request, id):

	context = {
		'user': User.objects.get(id= id),
		'trips': Join.objects.filter(user=id),
		'alltrips' : Trips.objects.all()
	}
	return render(request, 'welcome.html', context)

def viewtrip(request, id):
	context = {
		'trips' :Trips.objects.get(id = id),
		'joined' :Join.objects.filter(trip = id)
	}

	return render(request, 'viewtrip.html', context)

def addtrip(request, id):
	context = {
		'user': User.objects.get(id = id)
	}
	return render(request, 'addtrip.html', context)
	##render goes to html- redirect go to route
	#reverse only for redirect and takes named routes
	#kwargs needed for id in route
	# redirect doesn't take request object
def jointrip(request, id):
	my_trips = Trips.objects.get(id = id)
	current_user = User.objects.get(id = request.session['id'])
	already_joined=Join.objects.filter(user=current_user, trip=my_trips)
	if (len(already_joined)) < 1:
		Join.objects.create(user=current_user, trip=my_trips)
	else:
		messages.warning(request, "You are already signed up for this trip!")
	return redirect(reverse('display',kwargs={'id': current_user.id}))
	
def createtrip(request, id):
	logged_in_user = User.objects.get(id = id)
	Trips.objects.create(name=request.POST['name'],
		plan=request.POST['plan'], travel_start=request.POST['travel_start'],travel_end=request.POST['travel_end'], my_trips=User.objects.get(id = id))
	Join.objects.create(user=logged_in_user, trip=Trips.objects.last())
	return redirect(reverse('display',kwargs={'id': id }))

def deletetrip(request, id):
	deletedtrip = Trips.objects.get(id=id)
	deletedtrip.delete()
	return redirect(reverse('display', kwargs={'id': id}))

def logout(request, id):
	request.session.flush()
	return redirect('index')

