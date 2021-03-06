# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='changetracker',
            options={'verbose_name': 'Change Tracker', 'verbose_name_plural': 'Change Tracking'},
        ),
        migrations.AlterModelOptions(
            name='filetracker',
            options={'verbose_name': 'File Tracker', 'verbose_name_plural': 'File Tracking'},
        ),
        migrations.AlterModelOptions(
            name='ncvhis',
            options={'verbose_name': 'NC Voter History', 'verbose_name_plural': 'NC Voter Histories'},
        ),
        migrations.AlterModelOptions(
            name='ncvoter',
            options={'verbose_name': 'NC Voter', 'verbose_name_plural': 'NC Voters'},
        ),
        migrations.AddField(
            model_name='filetracker',
            name='county_num',
            field=models.IntegerField(null=True),
        ),
    ]
