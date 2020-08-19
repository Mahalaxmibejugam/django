from django.contrib import admin
from django.urls import  path
from django.conf.urls import include,url
from mycontacts import views
urlpatterns = [
	url(r'name.*', views.name,name='name'),
	url(r'number.*',views.number,name='number'),
]