from django.db import models
from django.urls import reverse
from uauth.models import Customers


class Article(models.Model):
 	title		=	models.CharField(max_length=120)
 	content		=	models.TextField(blank=True,null=True)
 	author_name	=	models.CharField(max_length=120)
 	author 		= 	models.ForeignKey(Customers, on_delete=models.CASCADE)
 	active		=	models.BooleanField(default=True)

 	def get_absolute_url_view_article(self):
 		return reverse("product-view",kwargs={"id":self.id})
 	def get_absolute_url_delete_article(self):
 		return reverse("product-delete",kwargs={"id":self.id})
 	def get_absolute_url_edit_article(self):
 		return reverse("product-edit",kwargs={"id":self.id})
 	def get_absolute_url_article(self):
 		return reverse("product-list",kwargs={})