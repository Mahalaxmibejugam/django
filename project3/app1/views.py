from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def home(request):
	return render(request, 'app1/home.html')
def count(request):
	mytext=request.GET['fulltext']
	wcount=len(mytext.split())
	myList=[('rn1','Maha'), ('rn2','Ram'),('rn3','Shyam'),('rn4','Sam')]
	return render(request, 'app1/count.html',{'mycount':wcount , 'yourlist' :myList})