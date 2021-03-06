from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class RegistrationManager(models.Manager):
	def registration_validator(self, postData, request):
		passFlag = True
		if not postData['first_name'].isalpha():
			messages.warning(request, 'First name needs to be letters only')
			passFlag = False
		if len(postData['first_name']) < 2:
			messages.warning(request, 'First name is not long enough')
			passFlag =  False
		if not postData['last_name'].isalpha():
			messages.warning(request, "Last name needs to be letters only")
			passFlag = False
		if len(postData['last_name']) < 2:
			messages.warning(request, 'Last name is not long enough')
			passFlag = False
		if not EMAIL_REGEX.match(postData['email']):
			messages.warning(request, 'Email is not valid')
			passFlag = False
		if len(postData['password']) < 8:
			messages.warning(request, 'Password should be at least 8 characters')
			passFlag = False
		if postData['password'] != postData['confirm_pass']:
			messages.warning(request, 'Confirmation does not match Password')
			passFlag = False
		if User.objects.filter(email = postData['email']):
			messages.warning(request, 'This email already exists')
			passFlag = False

		if passFlag == True:
			messages.success(request, "Success! Welcome, " + postData['first_name'] + '!')
			encrypt = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt()).decode()
			User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = encrypt)
		return passFlag

	def login_validator(self, postData, request):
		passFlag = True
		if User.objects.filter(email = postData['email_login']):
			hashed = User.objects.get(email = postData['email_login']).password
			hashed = hashed.encode('utf-8')
			password = postData['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				messages.success(request, "Success! welcome, " + User.objects.get(email = postData['email_login']).first_name + "!")
				passFlag = True
			else:
				messages.warning(request, "Login Failed")
				passFlag = False
		else:
			messages.warning(request, "Login Failed")
			passFlag = False
		return passFlag
	

class User(models.Model):
	first_name=models.CharField(max_length=25)
	last_name=models.CharField(max_length=25)
	email=models.CharField(max_length=25)
	password=models.CharField(max_length=8)
	pass_confirm=models.CharField(max_length=8)
	
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects = RegistrationManager()

class ApptManager(models.Manager):
	def appt_validator(self, postData, request):
		passVal = True
		if len(postData['task']).isalpha():
			messages.warning(request, "Task can only have letters")
			passVal = False
		if passVal == True:
			messages.success(request, "Appointment has been accepted!")
			Appointment.objects.create(task = postData['task'], date = postData['date'])
		return passFlag

class Appointment(models.Model):
	task = models.CharField(max_length =255)
	date = models.DateTimeField()
	creator= models.ForeignKey(User, related_name="created_appt", on_delete=models.CASCADE)
	
	created_at= models.DateTimeField(auto_now_add =True)
	updated_at= models.DateTimeField(auto_now = True)

	objects = ApptManager()