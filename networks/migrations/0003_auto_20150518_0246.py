# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0002_auto_20150518_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='logo',
            field=models.ImageField(upload_to='networks/logos', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='logo',
            field=models.ImageField(upload_to='networks/logos', blank=True, null=True),
        ),
    ]
