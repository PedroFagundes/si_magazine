# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

class Posts(models.Model):
	title 	   = models.CharField('Título', max_length=100, null=False, blank=False)
	image_link = models.CharField('Imagem', max_length=200)
	post_body  = models.TextField(max_length=10000)
	tags       = models.ManyToManyField('Tags')
	author     = models.ForeignKey(User)
	pub_date   = models.DateField()
	is_active  = models.BooleanField(default=True)
	slug       = models.SlugField(blank=True)

	def __str__(self):
		return self.title

	# Overriding save method to set the slug field value
	def save(self):
		super(Posts, self).save()
		self.slug = '%s' % (slugify(self.title))
		super(Posts, self).save()

class Tags(models.Model):
	name = models.CharField('Tag', max_length=50)

	def __str__(self):
		return self.name