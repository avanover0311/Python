from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string



def index(request):
	context = {
		"time": strftime("%Y-%m-%d %H:%M %p")
		}
	return render(request,'first_app/index.html', context)