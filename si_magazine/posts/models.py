# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Posts(models.Model):
	title 	           = models.CharField(max_length=100, null=False, blank=False)
	image_link         = models.CharField(max_length=200)
	short_description  = models.TextField(max_length=10000)
	content            = RichTextField()
	author             = models.ForeignKey(User)
	tags               = models.ManyToManyField('Tags')
	category           = models.ForeignKey('Categories')
	pub_date           = models.DateField()
	pub_hour           = models.TimeField()
	is_active          = models.BooleanField(default=True)
	slug               = models.SlugField(blank=True)

	def __str__(self):
		return self.title

	# Overriding save method to set the slug field value
	def save(self):
		super(Posts, self).save()
		self.slug = '%s' % (slugify(self.title))
		super(Posts, self).save()

class Tags(models.Model):
	name  = models.SlugField(blank=True)
	label = models.CharField(max_length=50)

	def __str__(self):
		return self.label

	def save(self):
		super(Tags, self).save()
		self.name = '%s' % (slugify(self.label))
		super(Tags, self).save()

class Categories(models.Model):
	name  = models.SlugField(blank=True)
	label = models.CharField(max_length=50)

	def __str__(self):
		return self.label