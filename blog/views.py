from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from uauth.models import Customers
from .forms import ArticleForm,RawArticleForm

def article_list_view(request):
	if request.session.has_key('username'):
		if request.method == "POST":
			search=request.POST.get('search')
			queryset=Article.objects.filter(title__contains=search)
			print(queryset)
			context={
				"object_list":queryset,
				"search":search,
				"blog_page":"active",
				"navbar":request.session['name']
			}
			return render(request,'articles/list.html',context)
		else:	
			queryset=Article.objects.all()
			#print(obj)
			context={
				"object_list":queryset,
				"blog_page":"active"
			}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/list.html',context)
	else:
		return redirect('ulogin')

def article_details_view(request,id):
	if request.session.has_key('username'):
		obj=Article.objects.get(id=id)
		#print(obj)
		context={
			"object_list":queryset,
			"blog_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/detail.html',context)
	else:
		return redirect('ulogin')

#####Using Form Model

def article_create_view(request):
	if request.session.has_key('username'):
		initial_data={
			'title':"Test Product"
		}
		if request.method == "POST":	
			form = ArticleForm(request.POST or None,initial=initial_data)
			if form.is_valid():
				cus=Customers.objects.get(id=request.session['id'])
				res=Article(
					title=form.cleaned_data['title'],
					content=form.cleaned_data['content'],
					author=cus,
					author_name=request.session['username'],
					active=True
					)
				res.save()
				form = ArticleForm()
			context={
				"form":form,
				"blog_page":"active"
			}
		else:
			print(request.GET)
			form = ArticleForm()
			context={"form":form}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/create.html',context)
	else:
		return redirect('ulogin')

def article_edit_view(request,id):
	if request.session.has_key('username'):
		initial_data={
			'title':"Test Product"
		}
		if request.method == "POST":	
			form = ArticleForm(request.POST or None,initial=initial_data)
			if form.is_valid():
				res=Article.objects.get(id=id)
				res.title=form.cleaned_data['title']
				res.content=form.cleaned_data['content']
				res.author_name=request.session['username']
				res.active=True
				res.save()	
				return redirect('article-list')		
			form = ArticleForm()
			context={
				"form":form,
				"blog_page":"active"
			}
		else:
			print(request.GET)
			search=request.POST.get('search')
			obj =get_object_or_404(Article,id=id)
			form = ArticleForm(instance=obj)
			form.id=id
			context={
				"form":form,
				"object":obj,
				"blog_page":"active"
				}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/edit.html',context)
	else:
		return redirect('ulogin')


def article_view(request,id):
	if request.session.has_key('username'):
		# obj=Article.objects.get(id=id)
		obj=get_object_or_404(Article,id=id)
		# try:
		# 	obj=Article.objects.get(id=id)
		# except Article.DoesNotExist:
		# 	raise Http404
		context={
			'object':obj,
			"blog_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/detail.html',context)
	else:
		return redirect('ulogin')	

#delete view

def article_delete_view(request,id):
	if request.session.has_key('username'):
		obj=get_object_or_404(Article,id=id)
		if request.method=="POST":
			obj.delete()
			return redirect('article-list')
		context={
			'object':obj,
			"blog_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/article_delete.html',context)
	else:
		return redirect('ulogin')
