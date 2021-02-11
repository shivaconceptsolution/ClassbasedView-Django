from django.db import models
from django.urls import reverse
class SCSModel(models.Model): 

	# fields of the model 
	title = models.CharField(max_length = 200) 
	description = models.TextField()

	# renames the instances of the model 
	# with their title name 
	def __str__(self): 
		return str(self.id) + self.title + str(self.description)
	def get_absolute_url(self):
		return reverse('hello')
