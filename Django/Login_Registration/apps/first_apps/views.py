from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *


def index(request):
    response = "Hello, I am your first request!"
    return render(request, 'first_apps/index.html')

def create(request):
	print(request.POST)
	errors = User.objects.register_validate(request.POST)

	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		User.objects.create(first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],email=request.POST['email'],
			password=request.POST['password']) 
		user = User.objects.get(email=request.POST['email'])
		request.session['first_name'] = user.first_name
		request.session['id'] = user.id

		return redirect('/trips')

def login(request):
	print(request.POST)

	err = User.objects.login_validate(request.POST)
	print(err)

	if 'uid'  not in err:
		for key, value in err.items():
			print('key:', key, 'value:', value)
			messages.error(request, value)
			return redirect('/')
	user = User.objects.get(email=request.POST['email_login'])
	request.session['first_name'] = user.first_name
	request.session['id'] = user.id

	return redirect('/trips/')			


def update(req, id):

	user =User.objects.get(id = id)
	user.last_name = 'changed name'
	user.save()
	print(user)
	return redirect('/')

def trips(request):
	
	return render(request, 'first_apps/trips.html')


def addtrips(request):

	return render(request, 'first_apps/addtrip.html')
	print(request.POST)

def createtrips():
	Trips.objects.create(destination=request.POST['name'],
		description=request.POST['plan'], date_from=request.POST['travel_start'],
		date_to=request.POST['travel_end'])

def viewtrip(request):

	return render(request, 'first_apps/viewtrip.html')
	print(request.POST)

def logout(request):
	request.session.flush()
	return redirect('/')
