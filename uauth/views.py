from django.http import Http404,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Users
from .forms import UserLoginForm,UserRegistrationForm

#####Using Form Model

def login_view(request):
	if request.method == "POST":	
		form = UserLoginForm(request.POST or None)
		if form.is_valid():	
			# return HttpResponse(form.cleaned_data.get("email_id"))
			# res=Users.objects.get(email_id=form.cleaned_data.get("email_id"))
			form.email_id=form.cleaned_data.get("email_id")
			form.password=form.cleaned_data.get("password")
	else:
		print(request.GET)
		form = UserLoginForm()
		context={
				"form":form,
				"login_form":"active"
			}
	return render(request,'uauth/login.html',context)

def register_view(request):
	if request.method == "POST":	
		context={
			"register_page":"active",
			"status":"true"
			}
		form = UserRegistrationForm(request.POST or None)
		global email
		if form.is_valid(): 
			# return HttpResponse(form.cleaned_data.get("email_id"))
			data={
				"email_id":form.cleaned_data.get("email_id"),
				"password":form.cleaned_data.get("password"),
				"repassword":form.cleaned_data.get("repassword"),
				"user_type":2,
				"active":"true"
			}
			email=data.get('email_id', "")
			#return HttpResponse(data.items())
			if data.get("password","") != data.get("repassword", ""):
				context.update({'message':"Password missmatch!"})
				context.update({'status':"flase"})
			Usersqueryset=Users.objects.filter(email_id__contains=email)
			if Usersqueryset:
				context.update({'message':"Email already used!"})
				context.update({'status':"flase"})
			data.pop("repassword", None)
			#return HttpResponse(context.items())
			if context.status == "true":
				status=Users.objects.create(data)
			return HttpResponse(status)
	else:
		form = UserRegistrationForm()
		context={
			"form":form,
			"register_page":"active"
			}
	return render(request,'uauth/register.html',context)

