# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0004_auto_20150518_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='locale',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, help_text="If different from '{network} {locale}'."),
        ),
    ]
