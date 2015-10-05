# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth import logout as auth_logout

from posts.models import Posts, Tags, Categories

class Home(ListView):
	model         = Posts
	template_name = 'homesite/home.html'

	def get_context_data(self, **kwargs):
	    context                      = super(Home, self).get_context_data(**kwargs)
	    context['posts']             = Posts.objects.all()
	    if len(Posts.objects.all()) >= 8:
	    	for i in range(1,9):
	    		context['post_' + str(i)] = Posts.objects.all().order_by('-id')[i]
	    else:
	    	for i in range(1,len(Posts.objects.all())):
	    		context['post_' + str(i)] = Posts.objects.all().order_by('-id')[i]
	    context['interesting_posts'] = Posts.objects.all().order_by('image_link')[:12]
	    context['last_news_posts']   = Posts.objects.all().order_by('-id')[:10]
	    context['most_liked_posts']  = Posts.objects.all().order_by('content')[:3]
	    context['tags']              = Tags.objects.all()
	    context['categories']        = Categories.objects.all()
	    return context

class UserPanel(TemplateView):
	template_name = 'homesite/user-panel.html'

	def get_context_data(self, **kwargs):
	    context             = super(UserPanel, self).get_context_data(**kwargs)
	    if self.request.user.is_authenticated():
	    	context['my_posts'] = Posts.objects.filter(author=self.request.user)
	    else:
	    	context['my_posts'] = 'Não ta logado'
	    return context

def Logout(request):
	auth_logout(request)
	return redirect('/')

