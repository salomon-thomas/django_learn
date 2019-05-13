from django.db import models
from django.urls import reverse
class Customers(models.Model):
 	name		=	models.CharField(max_length=120)
 	email_id	=	models.CharField(max_length=120)
 	password	=	models.CharField(max_length=120)
 	user_type	=	models.DecimalField(max_digits=2,decimal_places=0)
 	active		=	models.BooleanField(default=True)

 	# def get_absolute_url_view(self):
 	# 	return reverse("product-view",kwargs={"id":self.id})
 	# def get_absolute_url_delete(self):
 	# 	return reverse("product-delete",kwargs={"id":self.id})
 	# def get_absolute_url_edit(self):
 	# 	return reverse("product-edit",kwargs={"id":self.id})
 	# def get_absolute_url_products(self):
 	# 	return reverse("product-list",kwargs={})
