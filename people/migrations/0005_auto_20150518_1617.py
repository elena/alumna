# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20150518_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='img_url',
        ),
        migrations.AddField(
            model_name='person',
            name='profile',
            field=models.ImageField(null=True, blank=True, upload_to='people/profile'),
        ),
    ]
