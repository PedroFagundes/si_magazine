# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import PostDetailView

urlpatterns = [
	url(r'^(?P<slug>[^\.]+)', PostDetailView.as_view(), name='post_detail')
]