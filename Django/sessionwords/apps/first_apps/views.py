from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	if 'activities' not in request.session:
		request.session['activities'] = []
	return render(request, "index.html")

def process(request):
	if 'big' in request.POST:
		bigfont = 50
	else:
		bigfont = 10
	temp_list = request.session['activities']
	temp_list.append({"word": request.POST['word'], 
		"color": request.POST['color'], "bigfont": ['big_font']})
	request.session['activities'] = temp_list
	return redirect('/')



def reset(request):
    request.session.flush()
    return redirect('/')