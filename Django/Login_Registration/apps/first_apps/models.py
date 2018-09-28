from __future__ import unicode_literals
from django.db import models
import bcrypt


class RegisterManager(models.Manager):
	def register_validate(self, postData):
		errors={}
		if len(postData['first_name']) <= 0:
			errors['first_name'] = 'Must have First Name'
		if len(postData['last_name']) <= 0:
			errors['last_name'] = 'Must have Last Name'
		if len(postData['email']) < 4:
			errors['email']	= 'Email must contain 4 characters'
		if (postData['email']) == (postData['email']):
			errors['email'] = 'User already exists'
		if len(postData['password']) < 8:
			errors['password'] = 'Password must contain 8 characters'
		return errors

	def login_validate(self, postData):
		error = {}
		try:
			user =User.objects.get(email=postData['email_login'])
		except User.DoesNotExist:
			error['email_login'] = 'Login Error'
			return error
		if user.password != (postData['password']):
			error['password'] = 'Login Error'
		return error



class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = RegisterManager()


class Trips(models.Model):
	name = models.CharField(max_length =255)
	travel_start = models.DateTimeField(auto_now_add =True)
	travel_end = models.DateTimeField(auto_now_add =True)
	plan = models.TextField()
	my_trips= models.ForeignKey(User, related_name="trips")
	
	created_at= models.DateTimeField(auto_now_add =True)
	updated_at= models.DateTimeField(auto_now = True)




