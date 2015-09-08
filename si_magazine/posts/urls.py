# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import PostsList, PostDetailView, PostsCategoryList, PostsTagList, EditPost, NewPost

urlpatterns = [
	url(r'^$', PostsList.as_view(), name='all_posts'),
	url(r'^new', NewPost.as_view(), name='new_post'),
	url(r'^edit/(?P<slug>[^\.]+)$', EditPost.as_view(), name='edit_post'),
	url(r'^category/([\w-]+)/$', PostsCategoryList.as_view(), name='posts_category_list'),
	url(r'^tag/([\w-]+)/$', PostsTagList.as_view(), name='posts_tag_list'),
	url(r'^(?P<slug>[^\.]+)', PostDetailView.as_view(), name='post_detail')
]