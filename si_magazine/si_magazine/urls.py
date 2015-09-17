# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from homesite.views import Home, UserPanel

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^panel/', UserPanel.as_view(), name='user_panel'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'homesite.views.Logout', name='logout'),
    url(r'^posts/', include('posts.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
