# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150518_1132'),
        ('people', '0003_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonEventRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=128)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.RemoveField(
            model_name='personevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='personevent',
            name='person',
        ),
        migrations.RemoveField(
            model_name='personrole',
            name='event',
        ),
        migrations.RemoveField(
            model_name='personrole',
            name='person',
        ),
        migrations.RemoveField(
            model_name='personrole',
            name='role',
        ),
        migrations.RemoveField(
            model_name='personskill',
            name='person',
        ),
        migrations.RemoveField(
            model_name='personskill',
            name='skill',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='description',
            new_name='desc_skill',
        ),
        migrations.AddField(
            model_name='person',
            name='desc_social',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='PersonEvent',
        ),
        migrations.DeleteModel(
            name='PersonRole',
        ),
        migrations.DeleteModel(
            name='PersonSkill',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AddField(
            model_name='personeventrole',
            name='person',
            field=models.ForeignKey(to='people.Person'),
        ),
    ]
