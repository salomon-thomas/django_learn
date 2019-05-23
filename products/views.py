from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,ExampleModel
from .forms import *
from django.contrib import messages

def product_list_view(request):
	if request.session.has_key('username'):
		if request.method == "POST":
			search=request.POST.get('search')
			queryset=Products.objects.filter(title__contains=search)
			print(queryset)
			context={
				"object_list":queryset,
				"search":search,
				"product_page":"active",
				"navbar":request.session['name']
			}
			return render(request,'products/list.html',context)
		else:	
			queryset=Products.objects.all()
			#print(obj)
			context={
				"object_list":queryset,
				"product_page":"active"
			}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/list.html',context)
	else:
		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')

def product_details_view(request,id):
	if request.session.has_key('username'):
		obj=Products.objects.get(id=id)
		#print(obj)
		context={
			"object_list":queryset,
			"product_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/detail.html',context)
	else:
		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')

#####Using Form Model

def product_create_view(request):
	if request.session.has_key('username'):
		initial_data={
			'title':"Test Product"
		}
		if request.method == "POST":
			# return HttpResponse(request.FILES['product_image'])	
			form = ProductAddForm(request.POST,request.FILES)
			# return HttpResponse(form.product_image)
			if form.is_valid():
				form.save()
				messages.success(request, 'New Product Added!')
				form = ProductAddForm()
			context={
				"form":form,
				"product_page":"active"
			}
		else:
			print(request.GET)
			form = ProductAddForm()
			context={"form":form}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/create.html',context)
	else:
		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')

def product_edit_view(request,id):
	if request.session.has_key('username'):
		initial_data={
			'title':"Test Product"
		}
		if request.method == "POST":
			# return HttpResponse("Tes")
			form = ProductAddForm(request.POST,request.FILES,initial=initial_data)
			if form.is_valid():
				print(form.cleaned_data)
				res=Products.objects.get(id=id)
				res.title=form.cleaned_data.get("title")
				res.description=form.cleaned_data.get("description")
				res.price=form.cleaned_data.get("price")
				res.featured=form.cleaned_data.get("featured")
				res.active=form.cleaned_data.get("active")
				res.product_image=form.cleaned_data.get("product_image")
				res.save()	
				messages.success(request, 'Product Details Updated!')
				return redirect('product-list')
			context={
				"form":form,
				"product_page":"active"
			}
		else:
			print(request.GET)
			search=request.POST.get('search')
			obj =get_object_or_404(Products,id=id)
			form = ProductAddForm(instance=obj)
			form.id=id
			context={
				"form":form,
				"object":obj,
				"product_page":"active"
				}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/edit.html',context)
	else:

		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')




#### From Custom for not using form model
# def product_create_view(request):
# 	form= RawProductAddForm()
# 	if request.method == "POST":
# 		form= RawProductAddForm(request.POST)
# 		if form.is_valid():
# 			Products.objects.create(**form.cleaned_data)
# 			print(form.cleaned_data)
# 		else:
# 			print(form.errors)
# 	context={"form" : form }
# 	return render(request,'products/create.html',context)

# product edit view:

def product_view(request,id):
	if request.session.has_key('username'):
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
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/detail.html',context)
	else:
		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')	

#delete view

def product_delete_view(request,id):
	if request.session.has_key('username'):
		obj=get_object_or_404(Products,id=id)
		if request.method=="POST":
			obj.delete()
			return redirect('product-list')
		context={
			'object':obj,
			"product_page":"active"
		}
		context.update({'logged_in':'True','navbar':request.session['name']})
		return render(request,'products/product_delete.html',context)
	else:
		messages.error(request, 'Session TimeOut!')
		return redirect('ulogin')



def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel()
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    else:
    	return render(request,'test.html')
    # return HttpResponseForbidden('allowed only via POST')