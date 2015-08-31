# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from homesite.views import Home

urlpatterns = [
	url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include('posts.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
]