# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150518_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='code',
            field=models.CharField(null=True, blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(null=True, blank=True, max_length=128),
        ),
    ]
