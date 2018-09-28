from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, "first_app/index.html")


def randword(request):
	if request.method == "POST":
		randword = get_random_string(length=14)
		request.session['randword'] = randword
		request.session['count'] += 1
		return redirect('/')
	return HttpResponse ("Hello")

def reset(request):
	request.session.flush()
	return redirect('/')