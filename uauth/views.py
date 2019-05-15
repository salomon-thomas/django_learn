from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Customers
from .forms import UserLoginForm,UserRegistrationForm
from django.contrib import messages
import uuid
import hashlib

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
				Usersqueryset=Customers.objects.get(email_id=email_id)
				if Usersqueryset.email_id:
					if check_password(Usersqueryset.password, password):
						request.session['username']=Usersqueryset.email_id
						request.session['name']=Usersqueryset.name
						request.session['id']=Usersqueryset.id
						messages.success(request, 'Welcome to User Space')
						return redirect('product-list')
					else:
						messages.warning(request, 'Invalid Password')
						return redirect('ulogin')
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
			"status":True
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

			Usersqueryset=Customers.objects.filter(email_id=email)
			if password != repassword:
				context.update({'message':"Password missmatch!"})
				context.update({'status':False})
			elif Usersqueryset:
				context.update({'message':"Email already used!"})
				context.update({'status':False})

			# return HttpResponse(context.get('status',''))
			if context.get('status','') == True:
				# return HttpResponse(context.get('status',''))
				#return HttpResponse(context.get('query_status',''))
				users.password=hash_password(password)

				status=users.save()
				messages.success(request, 'Account Created!')
				return redirect('ulogin')
			else:
				messages.warning(request,context.get('message',''))
				return redirect('uregister')
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

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
