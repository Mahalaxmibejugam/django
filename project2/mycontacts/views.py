from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def name(request):
	return HttpResponse('<h1>Name will be displayed</h1>')

def number(request):
	return HttpResponse('<h1>Number will be displayed</h1>')

