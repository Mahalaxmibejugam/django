from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def home(request):
	return render(request, 'app1/home.html')
def count(request):
	mytext=request.GET['fulltext']
	wcount=len(mytext.split())
	vList=list("aeiouAEIOU")
	new_str=""
	new_count=0
	for i in mytext:
		if i in vList:
			new_count+=1
		else:
			new_str+=i
	myList=[('rn1','Maha'), ('rn2','Ram'),('rn3','Shyam'),('rn4','Sam')]
	return render(request, 'app1/count.html',{'count':wcount , 'myCount':new_count, 'mystr': new_str,'yourlist' :myList})