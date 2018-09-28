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
	 	User.objects.create(first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],email=request.POST['email'],
			password=request.POST['password']) 
	 	user = User.objects.get(email=request.POST['email'])
	 	return redirect(reverse('display',kwargs={'id': user.id }))
	 else:
	 	return redirect(reverse('index'))

def login(request):
	
	if User.objects.login_validator(request.POST, request):
		passFlag = True
		user = User.objects.get(email=request.POST['email_login'])
		return redirect(reverse('display',kwargs={'id': user.id }))
	else:
		return redirect(reverse('index',kwargs={'id': user.id }))

def display(request, id):
	context = {
		'user': User.objects.get(id= id),
		'quotes': Quote.objects.all()
	}
	return render(request, 'welcome.html', context)

def editaccount(req, id):

	user =User.objects.get(id = id)
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.email = request.POST['update_email']
	user.save()
	return redirect('display/')

def viewquotes(request, id):
	
	logged_in_user=User.objects.get(id= id)
	current_user= logged_in_user.created_quote.all()
	other_users= Quote.objects.exclude(creator=logged_in_user)
	context = {
		'logged_in_user' : logged_in_user,
		'current_user' : current_user,
		'other_users' : other_users,
		'quotes' : Quote.objects.all()
	}

	return render(reverse(request, 'viewquotes.html', context))

def addquote(request, id):
	logged_in_user = User.objects.get(id = id)
	Quote.objects.create(quote=request.POST['quote'], author=request.POST['author'],
			creator= logged_in_user)

	return redirect(reverse('display',kwargs={'id': id }))

def deletequote(request, id):
	quote=Quote.objects.get(id=id)
	quote.delete()
	return redirect(reverse('display'))

def logout(request, id):
	flush()
	return redirect(reverse('index', kwargs={'id': id}))
