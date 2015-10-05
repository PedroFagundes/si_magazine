# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150904_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='label',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='label',
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 10, 54, 53, 408529)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_hour',
            field=models.TimeField(default=datetime.datetime(2015, 10, 5, 10, 54, 53, 408590)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.SlugField(),
        ),
    ]
