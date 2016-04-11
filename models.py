from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class User_Profile(models.Model):
	user = models.ForeignKey(User)
	profilePic = models.TextField(default='https://s3-us-west-1.amazonaws.com/molly1murphy/stripevetar.png')
	def __str__(self):
		print str(self.user)
		return str(self.user)

class Match(models.Model):
	user = models.ForeignKey(User,null=True)
	userGuesses = models.IntegerField()
	win = models.BooleanField()  
	winningWord = models.CharField(max_length=8)
	def __str__(self):
		  return self.name
