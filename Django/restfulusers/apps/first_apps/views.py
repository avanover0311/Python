from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import *
# Create your views here.
def index(request):
	response="up and running"
	context={
	'users':User.objects.all()
	}
	return render(request, 'index.html', context)

def adduser(request):
	
	return render(request, 'adduser.html')

def create(request):
	User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
	return redirect( '/')

def display(request, id):
	context = {
		'users': User.objects.get(id= id)
	}
	return render(request, 'viewuser.html', context)

def edituser(request, id):
	context = {
		'users': User.objects.get(id=id)
	}
	return render(request, 'edituser.html', context)

def updateuser(request, id):
	user =User.objects.get(id = id)
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['email']
	user.save()
	return redirect('/')

def deleteuser(request, id):
	user = User.objects.get(id = id)
	user.delete()
	return redirect('/')
	


