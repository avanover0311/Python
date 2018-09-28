from django.db import models
from django.contrib import admin

class User(models.Model):
	first_name =models.CharField(max_length = 255)
	last_name= models.CharField(max_length = 255)
	email = models.CharField(max_length= 255)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __repr__(self):
		return f'User(first_name={self.first_name}, last_name={self.last_name})'

class Book(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()

	uploaded_by = models.ForeignKey(User, related_name = 'uploads')
	liked_by = models.ManyToManyField(User, related_name ='books_liked')

	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now = True)

	def__repr__(self):
		return f'Book(name={self.name}, desc={self.desc})'
	


