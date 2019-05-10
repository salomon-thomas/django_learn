from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.
def home_view(request,*args , **kwargs):
	print(request.user)
	my_context={
		"title":"This is Home Page",
		"year":2019,
		"home_page":"active"
	}
	return render(request,'home.html',my_context)

def contact_view(request,*args , **kwargs):
	my_context={
		"title":"This is Contact US",
		"year":2019,
		"contact_page":"active"
	}
	return render(request,'contacts.html',my_context)

def about_view(request,*args , **kwargs):
	my_context={
		"title":"This is About US",
		"year":2019,
		"my_list":[100,125,2587,457879,'jango'],
		"about_page":"active"
	}
	return render(request,'about.html',my_context)

def blog_view(request,*args , **kwargs):
	my_context={
		"title":"This is BlogS",
		"year":2019,
		"blog_page":"active"
	}
	return render(request,'blog.html',my_context)
