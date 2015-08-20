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
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('image_link', models.CharField(max_length=200, verbose_name='Imagem')),
                ('post_body', models.TextField(max_length=10000)),
                ('pub_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='posts.Tags'),
        ),
    ]
