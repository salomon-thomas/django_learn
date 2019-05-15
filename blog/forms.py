from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label="Article Name",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"Article Title Eg: My First Blog",
			'style':"width:280px"
			})
		)
	content = forms.CharField(
		label="content",
		widget=forms.Textarea(attrs={
		'class':"form-control"
		})
	)
	class Meta:
		model = Article
		fields = [
			'title',
			'content',
		]
	# def clean_title(self,*args,**kwargs):
	# 	title=self.cleaned_data.get('title')
	# 	if not "habel" in title:
	# 		raise forms.ValidationError("This Title is Invalid")
	# 	return title
			


class RawArticleForm(forms.Form):
	title = forms.CharField(
		label="Article Name",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"Article Title Eg: My First Blog",
			'style':"width:280px"
			})
		)
	content = forms.CharField(
		label="content",
		widget=forms.Textarea(attrs={
		'class':"form-control"
		})
	)
	price =forms.DecimalField(label="Item Price",initial="199")