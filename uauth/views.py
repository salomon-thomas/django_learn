from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Customers
from .forms import UserLoginForm,UserRegistrationForm
from django.contrib import messages

#####Using Form Model

def login_view(request):
	if request.method == "POST":	
		form = UserLoginForm(request.POST or None)
		context={
			"login_page":"active"
		}
		if form.is_valid():	
			email_id=form.cleaned_data.get("email_id")
			password=form.cleaned_data.get("password")
			try:
				Usersqueryset=Customers.objects.get(email_id=email_id,password=password)
				if Usersqueryset.email_id:
					#print(Usersqueryset.email_id)
					request.session['username']=Usersqueryset.email_id
					request.session['name']=Usersqueryset.name
					#return HttpResponse(Usersqueryset.name)
					messages.success(request, 'Welcome to User Space')
					return redirect('product-list')
			except Customers.DoesNotExist:
				context.update({'status':False,'message':'Invalid Username/Password'})
	else:
		print(request.GET)
		form = UserLoginForm()
		context={
				"form":form,
				"login_page":"active",
				"data":100
			}
	return render(request,'uauth/login.html',context)

def register_view(request):
	if request.method == "POST":	
		context={
			"register_page":"active",
			"status":"True"
			}
		form = UserRegistrationForm(request.POST or None)
		global email
		if form.is_valid(): 
			# return HttpResponse(form.cleaned_data.get("email_id"))
			email=form.cleaned_data.get("email_id")
			password=form.cleaned_data.get("password")
			repassword=form.cleaned_data.get("repassword")
			users = Customers()
			users.name=form.cleaned_data.get("name")
			users.email_id=form.cleaned_data.get("email_id")
			users.password=form.cleaned_data.get("password")
			users.active=True
			users.user_type=2

			if password != repassword:
				context.update({'message':"Password missmatch!"})
				context.update({'status':"flase"})
			Usersqueryset=Customers.objects.filter(email_id__contains=email)
			if Usersqueryset:
				context.update({'message':"Email already used!"})
				context.update({'status':"flase"})
			if context.get("status","") == "True":
				status=users.save()
				context.update({'query_status':status})
			else:
				context.update({'query_status':False})

			if context.get('query_status','') != False:
				#return HttpResponse(context.get('query_status',''))
				return redirect('ulogin')
	else:
		form = UserRegistrationForm()
		context={
			"form":form,
			"register_page":"active"
			}
	return render(request,'uauth/register.html',context)


def logout_view(request):
	if request.method == "POST":
		request.session.flush()
		return redirect('ulogin')


