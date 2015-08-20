# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('image_link', models.CharField(max_length=200, verbose_name='Imagem')),
                ('post_body', models.TextField(max_length=10000, verbose_name='Corpo da Postagem')),
                ('pub_date', models.DateField()),
                ('pub_hour', models.TimeField()),
                ('is_active', models.BooleanField(verbose_name='Corpo da Postagem', default=True)),
                ('slug', models.SlugField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='posts.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='posts.Tags'),
        ),
    ]
