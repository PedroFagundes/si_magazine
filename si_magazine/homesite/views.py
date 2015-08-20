# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Posts, Tags, Categories

class Home(ListView):
	model         = Posts
	template_name = 'homesite/home.html'

	def get_context_data(self, **kwargs):
	    context               = super(Home, self).get_context_data(**kwargs)
	    context['posts']      = Posts.objects.all()
	    context['tags']       = Tags.objects.all()
	    context['categories'] = Categories.objects.all()
	    return context