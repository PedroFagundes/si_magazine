# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150821_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_body',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
