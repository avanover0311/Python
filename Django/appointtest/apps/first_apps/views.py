from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *
import datetime 
# Create your views here.
def index(request):
	return render(request,'index.html')

def create(request):
	if User.objects.registration_validator(request.POST, request):
	 	passFlag=True
	 	user = User.objects.get(email=request.POST['email'])
	 	request.session['id']=user.id
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
	todayappt= logged_in_user.created_appt.filter(date=datetime.date.today())
	nextappt= logged_in_user.created_appt.exclude(date=datetime.date.today())
	context = {
		'user': logged_in_user,
		'today_appt' : todayappt,
		'next_appt' : nextappt

	}
	return render(request, 'welcome.html', context)

def logout(request):
	request.session.flush()
	return redirect('index')

def createapp(request):
	logged_in_user= User.objects.get(id = request.session['id'])
	Appointment.objects.create(task =request.POST['task'], date=request.POST['date'], creator= logged_in_user, time=request.POST['time'])
	currentappts = Appointment.objects.filter(creator = logged_in_user)
	return redirect(reverse('display', kwargs={'id':logged_in_user.id}))

def editappt(request, id):
	context = {
		'appt': Appointment.objects.get(id =id)
	}
	return render(request,'editappt.html', context)

def updateappt(request, id):
	appt =Appointment.objects.get(id = id)
	appt.task = request.POST['task']
	appt.date = request.POST['date']
	appt.time = request.POST['time']
	appt.save()
	return redirect(reverse('display', kwargs={'id': id}))

def deleteappt(request, id):
	deletedappt = Appointment.objects.get(id=id)
	deletedappt.delete()
	return redirect(reverse('display', kwargs={'id': id}))






