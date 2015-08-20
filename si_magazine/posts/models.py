# -*- coding: utf-8 -*-
from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

class Posts(models.Model):
	title 	   = models.CharField('Título', max_length=100, null=False, blank=False)
	image_link = models.CharField('Imagem', max_length=200)
	post_body  = models.TextField('Corpo da Postagem', max_length=10000)
	author     = models.ForeignKey(User)
	tags       = models.ManyToManyField('Tags')
	category   = models.ForeignKey('Categories')
	pub_date   = models.DateField()
	pub_hour   = models.TimeField()
	is_active  = models.BooleanField('Corpo da Postagem', default=True)
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

class Categories(models.Model):
	name = models.CharField('Category', max_length=50)

	def __str__(self):
		return self.name