# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Posts, Tags, Categories

class Home(ListView):
	model         = Posts
	template_name = 'homesite/home.html'

	def get_context_data(self, **kwargs):
	    context                   = super(Home, self).get_context_data(**kwargs)
	    context['posts']          = Posts.objects.all()
	    context['1st_post']       = Posts.objects.all().order_by('-id')[0]
	    context['2nd_post']       = Posts.objects.all().order_by('-id')[1]
	    context['3rd_post']       = Posts.objects.all().order_by('-id')[2]
	    context['4th_post']       = Posts.objects.all().order_by('-id')[3]
	    context['5th_post']       = Posts.objects.all().order_by('-id')[4]
	    context['6th_post']       = Posts.objects.all().order_by('-id')[5]
	    context['7th_post']       = Posts.objects.all().order_by('-id')[6]
	    context['8th_post']       = Posts.objects.all().order_by('-id')[7]
	    context['whatsnew_posts'] = Posts.objects.all()[:10]
	    context['tags']           = Tags.objects.all()
	    context['categories']     = Categories.objects.all()
	    return context