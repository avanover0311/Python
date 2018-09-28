from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
	response = "up and running"
	return HttpRepsonse(response)