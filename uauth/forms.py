from django import forms

from .models import Customers


class UserLoginForm(forms.Form):
	email_id = forms.CharField(
		label="Username",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"username",
			'style':"width:280px"
			})
		)
	password = forms.CharField(
		label="Password",
		widget=forms.TextInput(attrs={
		'class':"form-control",
		'placeholder':"username",
		'style':"width:280px"
		})
	)
class UserRegistrationForm(forms.Form):
	email_id = forms.CharField(
		label="Username",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"username",
			'style':"width:280px"
			})
		)	
	name = forms.CharField(
		label="Name",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"Name",
			'style':"width:280px"
			})
		)
	password = forms.CharField(
		label="Password",
		widget=forms.TextInput(attrs={
		'class':"form-control",
		'placeholder':"password",
		'style':"width:280px"
		})
	)
	repassword = forms.CharField(
		label="Password",
		widget=forms.TextInput(attrs={
		'class':"form-control",
		'placeholder':"password",
		'style':"width:280px"
		})
	)