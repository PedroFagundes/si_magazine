# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.conf import settings
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image_link', models.CharField(max_length=200)),
                ('short_description', models.TextField(max_length=10000)),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_date', models.DateField(default=datetime.datetime(2015, 10, 5, 12, 57, 28, 195887))),
                ('pub_hour', models.TimeField(default=datetime.datetime(2015, 10, 5, 12, 57, 28, 195947))),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True, max_length=100, blank=True)),
                ('author', models.ForeignKey(default=posts.models.get_current_user, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='posts.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='posts.Tags'),
        ),
    ]
