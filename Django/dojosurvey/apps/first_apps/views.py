from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.



def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	return render(request, 'first_apps/index.html')


def process(request):
	request.session['count'] += 1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect('/success')

def success(request):
	return render(request, 'first_apps/success.html')
