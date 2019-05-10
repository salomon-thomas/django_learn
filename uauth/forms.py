from django import forms

from .models import Users


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
	password = forms.CharField(
		label="Password",
		widget=forms.TextInput(attrs={
		'class':"form-control",
		'placeholder':"username",
		'style':"width:280px"
		})
	)