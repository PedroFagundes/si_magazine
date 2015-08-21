# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='content',
            field=ckeditor.fields.RichTextField(default='Adicionado antes da implementação do ckeditor'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
