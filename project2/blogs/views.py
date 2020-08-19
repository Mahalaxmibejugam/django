from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def food(request):
	return HttpResponse('Eat good food and have good health')

def drinks(request):
	return HttpResponse('Drink 3L water..it keeps you hydrated')

