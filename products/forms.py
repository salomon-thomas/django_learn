from django import forms

from .models import Products,ExampleModel

class ProductAddForm(forms.ModelForm):
	title = forms.CharField(
		label="Product Name",
		widget=forms.TextInput(attrs={
			'class':"form-control",
			'placeholder':"Product Title Eg: Excel Protein Powder 500Mg",
			'style':"width:280px"
			})
		)
	description = forms.CharField(
		label="Description",
		widget=forms.Textarea(attrs={
		'class':"form-control"
		})
		)	
	product_image=forms.ImageField()
	class Meta:
		model = Products
		fields = [
			'title',
			'description',
			'price',
			'featured',
			'product_image',
			'active'
		]
	# def clean_title(self,*args,**kwargs):
	# 	title=self.cleaned_data.get('title')
	# 	if not "habel" in title:
	# 		raise forms.ValidationError("This Title is Invalid")
	# 	return title
			


# class RawProductForm(forms.Form):
# 	title = forms.CharField(
# 		label="Product Name",
# 		widget=forms.TextInput(attrs={
# 			'class':"form-control",
# 			'placeholder':"Product Title Eg: Excel Protein Powder 500Mg",
# 			'style':"width:280px"
# 			})
# 		)
# 	description = forms.CharField(
# 		label="Description",
# 		widget=forms.Textarea(attrs={
# 		'class':"form-control"
# 		})
# 	)
# 	price =forms.DecimalField(label="Item Price",initial="199")



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()