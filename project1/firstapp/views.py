from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def home(request):
	return HttpResponse('<h1> This is my page</h1>')
def aboutus(request):
	return HttpResponse('<h1>I go to 3rd year B.E IT in vasavi</h1>')
def hobbies(request):
	return HttpResponse('<h1> My hobbies are listening to music and playing badminton</h1>')