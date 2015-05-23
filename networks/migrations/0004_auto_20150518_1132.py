# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0003_auto_20150518_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='network',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
