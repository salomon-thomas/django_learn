from django.db import models
from django.urls import reverse
class Products(models.Model):
 	title			=	models.CharField(max_length=120)
 	description		=	models.TextField(blank=True,null=True)
 	price			=	models.DecimalField(max_digits=15, decimal_places=2)
 	active			=	models.BooleanField(default=True)
 	product_image	= 	models.ImageField(upload_to='product_images/',default = 'pic_folder/None/no-img.jpg')
 	featured		=	models.BooleanField(default=True)

 	def get_absolute_url_view(self):
 		return reverse("product-view",kwargs={"id":self.id})
 	def get_absolute_url_delete(self):
 		return reverse("product-delete",kwargs={"id":self.id})
 	def get_absolute_url_edit(self):
 		return reverse("product-edit",kwargs={"id":self.id})
 	def get_absolute_url_products(self):
 		return reverse("product-list",kwargs={}) 	
 	def get_absolute_url_test(self):
 		return reverse("upload_pic",kwargs={})

class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')