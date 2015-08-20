# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Posts

class Home(ListView):
	model = Posts
	context_object_name = 'posts'
	template_name = 'homesite/home.html'