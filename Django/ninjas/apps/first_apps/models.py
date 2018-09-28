from __future__ import unicode_literals
from django.db import models



class Dojo(models.Model):
	name=models.CharField(max_length = 25)
	city=models.CharField(max_length = 25)
	state=models.CharField(max_length = 2)
	created_at =models.DateTimeField(auto_now_add=True)
	updated_at =models.DateTimeField(auto_now=True)
# Create your models here.

class Ninjas(models.Model):
	first_name=models.CharField(max_length = 255)
	last_name=models.CharField(max_length = 255)
	dojo= models.ForeignKey(Dojo, related_name='ninjas')
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at= models.DateTimeField(auto_now= True)


class desc(models.Model):
	
