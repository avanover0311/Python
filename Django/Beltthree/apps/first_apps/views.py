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
	# otherswishe=Wish.objects.exclude(my_wishes=logged_in_user)
	context = {
		'user': logged_in_user,
		'mywishes': Join.objects.filter(user=logged_in_user),
		'otherwishes' : Wish.objects.exclude(all_wish=id)
	}
	return render(request, 'welcome.html', context)

def logout(request):
	request.session.flush()
	return redirect('index')

def viewwish(request, id):
	context = {
		'allwish' :Wish.objects.get(id = id),
		'joined_wish' :Join.objects.filter(wish = id)
	}

	return render(request, 'viewwish.html', context)

def addwish(request, id):
	context = {
		'user': User.objects.get(id = id)
	}
	return render(request, 'addwish.html', context)

def joinwish(request, id):
	my_wishes = Wish.objects.get(id = id)
	current_user = User.objects.get(id = request.session['id'])
	already_joined=Join.objects.filter(user=current_user, wish=my_wishes)
	if (len(already_joined)) < 1:
		Join.objects.create(user=current_user, wish=my_wishes)
	else:
		messages.warning(request, "You are already signed up for this wish!")
	return redirect(reverse('display',kwargs={'id': current_user.id}))

def createwish(request):
	logged_in_user= User.objects.get(id = request.session['id'])
	if User.objects.wish_validator(request.POST, request):
		passVal = True	
		Wish.objects.create(item =request.POST['item'], my_wishes=User.objects.get(id =request.session['id']))
		Join.objects.create(user=logged_in_user, wish=Wish.objects.last())
		my_wishes = Wish.objects.filter(my_wishes = logged_in_user)
		return redirect(reverse('display', kwargs={'id':logged_in_user.id}))
	else:
		messages.warning(request, "You need a wish")
	return render(request, 'addwish.html')

def removewish(request, id):
	deletedwish = Wish.objects.get(id=id)
	deletedwish.delete()
	return redirect(reverse('display', kwargs={'id': id}))






