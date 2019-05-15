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
				"article_page":"active",
				"navbar":request.session['name']
			}
			return render(request,'articles/list.html',context)
		else:	
			queryset=Article.objects.all()
			#print(obj)
			context={
				"object_list":queryset,
				"article_page":"active"
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
			"article_page":"active"
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
				res=Article.objects.get()
				cus=Customers.objects.get(id=request.session['id'])
				res.title=form.cleaned_data['title']
				res.content=form.cleaned_data['content']
				res.author_name=request.session['username']
				res.author=cus
				res.active=True
				res.save()
				return HttpResponse(res)
				# form.cleaned_data['active']=True
				# form.cleaned_data['author']=request.session['id']
				# form.cleaned_data['author_id']=request.session['id']
				# form.cleaned_data['author_name']=request.session['username']
				# print(form.cleaned_data)
				# form.save()
				# Article.objects.create(form.cleaned_data)
				form = ArticleForm()
			context={
				"form":form,
				"article_page":"active"
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
				print(form.cleaned_data)
				res=Article.objects.get(id=id)
				# return HttpResponse(res.id)
				res.title=form.cleaned_data.get("title")
				res.description=form.cleaned_data.get("description")
				res.price=form.cleaned_data.get("price")
				res.featured=form.cleaned_data.get("featured")
				res.active=form.cleaned_data.get("active")
				res.save()			
				#form.id=id
				#form.save()
			form = ArticleForm()
			context={
				"form":form,
				"article_page":"active"
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
				"article_page":"active"
				}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/edit.html',context)
	else:
		return redirect('ulogin')




#### From Custom for not using form model
# def article_create_view(request):
# 	form= RawArticleForm()
# 	if request.method == "POST":
# 		form= RawArticleForm(request.POST)
# 		if form.is_valid():
# 			Article.objects.create(**form.cleaned_data)
# 			print(form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	context={"form" : form }
# 	return render(request,'articles/create.html',context)

# article edit view:

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
			"article_page":"active"
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
			"article_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'articles/article_delete.html',context)
	else:
		return redirect('ulogin')
