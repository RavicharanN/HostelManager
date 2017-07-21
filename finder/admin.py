# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Student,Hostels,Status

class StudentAdmin(admin.ModelAdmin) :
	list_display = ["__unicode__"]
	class Meta:
		model = Student

class HostelsAdmin(admin.ModelAdmin) :
	list_display = ["__unicode__"]
	class Meta:
		model = Hostels

class StatusAdmin(admin.ModelAdmin) :
	list_display = ["__unicode__"]
	class Meta:
		model = Status

admin.site.register(Student,StudentAdmin)
admin.site.register(Hostels,HostelsAdmin)
admin.site.register(Status,StatusAdmin)

