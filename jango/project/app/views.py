from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def blog(request):
	return render(request,'blog.html')

def about(request):
	return render(request,'about.html')

def login(request):
	return render(request,'login.html')


