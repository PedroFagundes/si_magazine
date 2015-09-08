# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Posts, Categories, Tags
from .forms import PostForm

class NewPost(CreateView):
	form_class   = PostForm
	template_name = 'posts/new_post.html'

	def get_success_url(self):
		return reverse('home')

class EditPost(UpdateView):
	model         = Posts
	fields        = '__all__'
	template_name = 'posts/edit_post.html'
	success_url   = '/panel/'

class PostsList(ListView):
	model         = Posts
	template_name = 'posts/posts_list.html'

	def get_context_data(self, **kwargs):
		context = super(PostsList, self).get_context_data(**kwargs)
		context['posts']      = Posts.objects.all().order_by('-pub_date')
		context['categories'] = Categories.objects.all()
		context['tags']       = Tags.objects.all()
		return context

class PostDetailView(DetailView):
	model               = Posts
	context_object_name = 'post'
	template_name       = 'posts/post_detail.html'

	def get_context_data(self, **kwargs):
	    context               = super(PostDetailView, self).get_context_data(**kwargs)
	    this_post             = Posts.objects.filter(slug=self.kwargs['slug'])
	    context['categories'] = Categories.objects.all()

	    # Check if the post is the first, if yes, prev_post will be itself
	    if self.object.pk == 1:
	    	context['prev_post']  = get_object_or_404(Posts, id=1)
	    else:
	    	context['prev_post']  = get_object_or_404(Posts, id=(self.object.pk - 1))

	    # Check if the post is the last, if yes, next_post will be itself
	    if self.object.pk == len(Posts.objects.all()):
	    	context['next_post']  = get_object_or_404(Posts, id=(self.object.pk))
	    else:
	    	context['next_post']  = get_object_or_404(Posts, id=(self.object.pk + 1))
	    return context

class PostsCategoryList(ListView):
	template_name       = 'posts/posts_category_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		self.category = get_object_or_404(Categories, name=self.args[0])
		return Posts.objects.filter(category=self.category)

	def get_context_data(self, **kwargs):
	    context = super(PostsCategoryList, self).get_context_data(**kwargs)
	    self.category         = get_object_or_404(Categories, name=self.args[0])
	    context['category']   = self.category
	    context['categories'] = Categories.objects.all()
	    context['tags']       = Tags.objects.all()
	    return context

class PostsTagList(ListView):
	template_name       = 'posts/posts_tag_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		self.tag = get_object_or_404(Tags, name=self.args[0])
		return Posts.objects.filter(tags__name__contains=self.tag)

	def get_context_data(self, **kwargs):
	    context        = super(PostsTagList, self).get_context_data(**kwargs)
	    self.tag       = get_object_or_404(Tags, name=self.args[0])
	    context['tag'] = self.tag
	    context['categories'] = Categories.objects.all()
	    context['tags']       = Tags.objects.all()
	    return context