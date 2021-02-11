from django.shortcuts import render
from .models import SCSModel
from django.views.generic.edit import CreateView
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Data Inserted ")


class SCSCreate(CreateView): 

	# specify the model for create view 
	model = SCSModel 

	# specify the fields to be displayed 

	fields = ['title', 'description']


