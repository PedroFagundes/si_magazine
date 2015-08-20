# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Posts

class PostDetailView(DetailView):
	model               = Posts
	context_object_name = 'post'
	template_name       = 'posts/post_detail.html'

	def get_context_data(self, **kwargs):
	    context = super(PostDetailView, self).get_context_data(**kwargs)
	    return context

	def get_next(self):
	    next = Post.objects.filter(id__gt=self.id)
	    if next:
	      return next[0]
	    return False