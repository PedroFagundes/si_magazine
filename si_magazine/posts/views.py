# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Posts, Categories, Tags

class PostDetailView(DetailView):
	model               = Posts
	context_object_name = 'post'
	template_name       = 'posts/post_detail.html'

	def get_context_data(self, **kwargs):
	    context = super(PostDetailView, self).get_context_data(**kwargs)
	    context['categories'] = Categories.objects.all()
	    return context

class PostsCategoryList(ListView):
	template_name = 'posts/posts_category_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		self.category = get_object_or_404(Categories, name=self.args[0])
		return Posts.objects.filter(category=self.category)

	def get_context_data(self, **kwargs):
	    context = super(PostsCategoryList, self).get_context_data(**kwargs)
	    self.category = get_object_or_404(Categories, name=self.args[0])
	    context['category'] = self.category
	    return context

class PostsTagList(ListView):
	template_name = 'posts/posts_tag_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		self.tag = get_object_or_404(Tags, name=self.args[0])
		return Posts.objects.filter(tags__name__contains=self.tag)

	def get_context_data(self, **kwargs):
	    context = super(PostsTagList, self).get_context_data(**kwargs)
	    self.tag = get_object_or_404(Tags, name=self.args[0])
	    context['tag'] = self.tag
	    return context