# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0003_auto_20170529_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncvoter',
            name='birth_year',
            field=models.IntegerField(null=True),
        ),
    ]
