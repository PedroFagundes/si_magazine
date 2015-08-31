# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150821_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='label',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='label',
            field=models.CharField(default='teste', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image_link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='short_description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.SlugField(blank=True),
        ),
    ]
