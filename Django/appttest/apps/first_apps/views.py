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
	logged_in_user= User.objects.get(id = request.session['id'])
	context = {
		'user': logged_in_user,
		'allappts' : Appointment.objects.all(),
	}
	return render(request, 'welcome.html', context)

	##render goes to html- redirect go to route
	#reverse only for redirect and takes named routes
	#kwargs needed for id in route
	# redirect doesn't take request object
	#dont pull in an ID if something is being created in the function
def createappt(request):
	logged_in_user= User.objects.get(id = request.session['id'])
	Appointment.objects.create(task =request.POST['task'], date=request.POST['date'], creator= logged_in_user)
	currentappts = Appointment.objects.filter(creator = logged_in_user)
	return redirect(reverse('display', kwargs={'id':logged_in_user.id}))

def editappt(request, id):
	context = {
		'appt': Appointment.objects.get(id =id)
	}
	return render(request,'updateappt.html', context)

def updateappt(request, id):
	appt =Appointment.objects.get(id = id)
	appt.task = request.POST['task']
	appt.date = request.POST['date']
	appt.save()
	return redirect(reverse('display', kwargs={'id': id}))

def deleteappt(request, id):
	deletedappt = Appointment.objects.get(id=id)
	deletedappt.delete()
	return redirect(reverse('display', kwargs={'id': id}))

def logout(request):
	request.session.flush()
	return redirect('index')

