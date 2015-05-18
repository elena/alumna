# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='logo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/network/logos'), upload_to='', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='network',
            name='logo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/network/logos'), upload_to='', blank=True, null=True),
        ),
    ]
