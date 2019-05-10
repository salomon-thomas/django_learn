from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Products
from .forms import ProductForm,RawProductForm

def product_list_view(request):
	if request.method == "POST":
		search=request.POST.get('search')
		queryset=Products.objects.filter(title__contains=search)
		print(queryset)
		context={
			"object_list":queryset,
			"search":search,
			"product_page":"active"
		}
		return render(request,'products/list.html',context)
	else:	
		queryset=Products.objects.all()
		#print(obj)
		context={
			"object_list":queryset,
			"product_page":"active"
		}
		return render(request,'products/list.html',context)

def product_details_view(request,id):
	obj=Products.objects.get(id=id)
	#print(obj)
	context={
		"object_list":queryset,
		"product_page":"active"
	}
	return render(request,'products/detail.html',context)

#####Using Form Model

def product_create_view(request):
	initial_data={
		'title':"Test Product"
	}
	if request.method == "POST":	
		form = ProductForm(request.POST or None,initial=initial_data)
		if form.is_valid():
			print(form.cleaned_data)
			form.save()
			form = ProductForm()
		context={
			"form":form,
			"product_page":"active"
		}
	else:
		print(request.GET)
		form = ProductForm()
		context={"form":form}
	return render(request,'products/create.html',context)

def product_edit_view(request,id):
	initial_data={
		'title':"Test Product"
	}
	if request.method == "POST":	
		form = ProductForm(request.POST or None,initial=initial_data)
		if form.is_valid():
			print(form.cleaned_data)
			res=Products.objects.get(id=id)
			# return HttpResponse(res.id)
			res.title=form.cleaned_data.get("title")
			res.description=form.cleaned_data.get("description")
			res.price=form.cleaned_data.get("price")
			res.featured=form.cleaned_data.get("featured")
			res.active=form.cleaned_data.get("active")
			res.save()			
			#form.id=id
			#form.save()
		form = ProductForm()
		context={
			"form":form,
			"product_page":"active"
		}
	else:
		print(request.GET)
		search=request.POST.get('search')
		obj =get_object_or_404(Products,id=id)
		form = ProductForm(instance=obj)
		form.id=id
		context={
			"form":form,
			"object":obj,
			"product_page":"active"
			}
	return render(request,'products/edit.html',context)




#### From Custom for not using form model
# def product_create_view(request):
# 	form= RawProductForm()
# 	if request.method == "POST":
# 		form= RawProductForm(request.POST)
# 		if form.is_valid():
# 			Products.objects.create(**form.cleaned_data)
# 			print(form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	context={"form" : form }
# 	return render(request,'products/create.html',context)

# product edit view:

def product_view(request,id):
	# obj=Products.objects.get(id=id)
	obj=get_object_or_404(Products,id=id)
	# try:
	# 	obj=Products.objects.get(id=id)
	# except Products.DoesNotExist:
	# 	raise Http404
	context={
		'object':obj,
		"product_page":"active"
	}
	return render(request,'products/detail.html',context)	

#delete view

def product_delete_view(request,id):
	obj=get_object_or_404(Products,id=id)
	if request.method=="POST":
		obj.delete()
		return redirect('../products/list')
	context={
		'object':obj,
		"product_page":"active"
	}
	return render(request,'products/product_delete.html',context)
