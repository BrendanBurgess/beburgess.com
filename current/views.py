from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {}
	return render(request, 'current/index.html', context_dict)

def about(request):
	context_dict = {}
	return render(request, 'current/about.html', context_dict)

def projects(request):
	context_dict = {}
	return render(request, 'current/projects.html', context_dict)

def interests(request):
	context_dict = {}
	return render(request, 'current/interests.html', context_dict)

def poli(request):
	context_dict = {}
	return render(request, 'current/poli.html', context_dict)

def comp(request):
	context_dict = {}
	return render(request, 'current/comp.html', context_dict)

def contact(request):
	context_dict = {}
	return render(request, 'current/contact.html', context_dict)