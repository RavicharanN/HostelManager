# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hostels(models.Model) :
	HostelName = models.CharField(max_length=20,default='Select your Hostel',null=False)

	def __unicode__(self):
		return unicode(self.HostelName)


class Status(models.Model):
	StudentStatus = models.CharField(max_length=20,default=None,null=False)

	def __unicode__(self):
		return unicode(self.StudentStatus)		

class Student(models.Model) :
	name = models.CharField(max_length=50,default=None,null=False)
	RollNo = models.CharField(max_length=20,default=None,null=False)
	hostel = models.ForeignKey(Hostels,default=None,null=False)
	status = models.ForeignKey(Status,default=None,null=False)

	def __unicode__(self):
		return unicode(self.name)
