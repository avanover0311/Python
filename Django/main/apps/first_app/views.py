from django.shortcuts import render, HttpResponse

def index(request):
	response ="Hello!"

	return HttpResponse(response)
# Create your views here.







