from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def name(request):
	return HttpResponse('Name will be displayed')

def number(request):
	return HttpResponse('Number will be displayed')

