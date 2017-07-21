# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Student,Hostels,Status
from django.views.generic import View
from forms import StudentForm
# from forms import StudentForm

# Create your views here.
def index(request) :
	form = StudentForm(request.POST)
	if(request.method=='POST'):
		if(form.is_valid()):
			form.save()
			message = 'Successfully Registered'
			return render(request,'index.html',{'form': form,'message': message})

		else :
			form_error = "(Registration Failed. Have you filled all the details?)"
			return render(request,'index.html',{'form': form,'form_error': form_error})
	else :
		form = StudentForm(request.POST)
	return render(request,'index.html',{'form': form})

def details(request):
	object_list = Student.objects.all().order_by('status_id')
	bh1 = Student.objects.filter(hostel__id=1).order_by('status_id')
	bh2 = Student.objects.filter(hostel__id=2).order_by('status_id')
	bh3 = Student.objects.filter(hostel__id=3).order_by('status_id')
	bh4 = Student.objects.filter(hostel__id=4).order_by('status_id')
	gh1 = Student.objects.filter(hostel_id=5).order_by('status_id')
	gh2 = Student.objects.filter(hostel_id=6).order_by('status_id')

	return render(request,'detail.html',{'object_list':object_list,'bh1': bh1,'bh2': bh2,'bh3': bh3,'bh4': bh4,'gh1': gh1,'gh2': gh2,})