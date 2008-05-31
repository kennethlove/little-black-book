from django.db import models

class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=50)
	date_joined = models.DateField(auto_now_add=True)
	last_login = models.DateField(auto_now=True)
	
class Contact(models.Model):
	user = models.ForeignKey(User)
	is_primary = models.NullBooleanField()
	first_name = models.CharField(max_length=45, null=True)
	middle_name = models.CharField(max_length=45, null=True)
	last_name = models.CharField(max_length=45, null=True)
	nickname = models.CharField(max_length=45, null=True)
	maiden_name = models.CharField(max_length=45, null=True)
	photo = models.ImageField(upload_to='user_media/contact_photo/', null=True)
	notes = models.TextField(null=True)
	website = models.URLField(verify_exists=True, null=True)
	street = models.CharField(max_length=75, null=True)
	city = models.CharField(max_length=45, null=True)
	state = models.CharField(max_length=45, null=True)
	zip_postal = models.CharField(max_length=8, null=True)
	country = models.CharField(max_length=75, null=True)
	
class Phone(models.Model):
	contact = models.ForeignKey(Contact)
	number = models.CharField(max_length=20)
	location = models.CharField(max_length=45)
	
class Email(models.Model):
	contact = models.ForeignKey(Contact)
	address = models.EmailField()
	location = models.CharField(max_length=45)
	
class Web(models.Model):
	contact = models.ForeignKey(Contact)
	service = models.CharField(max_length=75)
	username = models.CharField(max_length=75)
	url = models.URLField(verify_exists=False)
	
class IM(models.Model):
	contact = models.ForeignKey(Contact)
	service = models.CharField(max_length=75)
	username = models.CharField(max_length=75)
	
class Company(models.Model):
	contact = models.ForeignKey(Contact)
	name = models.CharField(max_length=75)
	job_title = models.CharField(max_length=45, null=True)
	department = models.CharField(max_length=75, null=True)
	website = models.URLField(verify_exists=True, null=True)
	photo = models.ImageField(upload_to='user_media/bus_card_image/', null=True)
	street = models.CharField(max_length=75, null=True)
	city = models.CharField(max_length=45, null=True)
	state = models.CharField(max_length=45, null=True)
	zip_postal = models.CharField(max_length=8, null=True)
	country = models.CharField(max_length=75, null=True)