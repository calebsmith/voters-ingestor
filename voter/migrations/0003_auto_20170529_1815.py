# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0002_auto_20170529_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncvoter',
            name='birth_year',
            field=models.IntegerField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ncvoter',
            name='name_suffix_lbl',
            field=models.CharField(default='', max_length=30, verbose_name='name_suffix_lbl'),
            preserve_default=False,
        ),
    ]
