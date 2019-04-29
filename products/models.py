from django.db import models
class Product(models.Model):
	# Yes = 'yes'
 #    No 	= 'no'
 #    status = (
 #        (Yes, 	'yes'),
 #        (No, 	'no'),)
 	title		=	models.CharField(max_length=120)
 	description	=	models.TextField(blank=True,null=True)
 	price		=	models.DecimalField(max_digits=5, decimal_places=2)
 	active		=	models.BooleanField(default=True)
 	featured	=	models.BooleanField(default=True)