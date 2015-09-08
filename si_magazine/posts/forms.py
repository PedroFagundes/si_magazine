# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, TextInput, Select, SelectMultiple

from .models import Posts

class PostForm(ModelForm):
    class Meta:
        model   = Posts
        fields  = '__all__'
        exclude = ('slug', 'is_active', 'pub_date', 'pub_hour',)
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'image_link': TextInput(attrs={'class': 'form-control'}),
            'short_description': Textarea(attrs={'class': 'form-control'}),
            'tags': SelectMultiple(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }