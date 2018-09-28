from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Author(models.Model):
	first_name =models.CharField(max_length = 255)
	last_name= models.CharField(max_length = 255)
	email = models.CharField(max_length= 255)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __repr__(self):
		return f'Author(first_name={self.first_name}, last_name={self.last_name})'

class Book(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField()

	uploaded_by = models.ForeignKey(Author, related_name = 'uploads')
	liked_by = models.ManyToManyField(Author, related_name ='books_liked')

	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now = True)

	def __repr__(self):
		return f'Book(name={self.name}, desc={self.desc})'