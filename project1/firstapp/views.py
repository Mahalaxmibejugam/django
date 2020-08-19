from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def home(request):
	return HttpResponse('<h1> This is my home page. I am Mahalaxmi. My roll number:1602-18-737-080</h1>')
def aboutme(request):
	return HttpResponse('<h1>I am Mahalaxmi. I am in 3rd year graduating from VCE in the  stream of IT bearing roll number 1602-18-737-080</h1>')
def hobbies(request):
	return HttpResponse('<h1> I like to code, listen music and learn new things.</h1>')