from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def home(request):
	return render(request,'app1/home.html',{'name':'Maha'})
def aboutus(request):
	return render(request,'app1/about.html',{'userid':'mahauserid'})
def hobbies(request):
	return HttpResponse('<h1>I like to code, listen music and learn new things</h1>')