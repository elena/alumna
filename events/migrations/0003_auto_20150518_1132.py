# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='date_start',
        ),
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventrole',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
