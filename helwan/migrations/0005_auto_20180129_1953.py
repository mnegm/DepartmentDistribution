# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helwan', '0004_auto_20180123_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dep',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Computers'), (2, 'Communications')], default='2'),
        ),
    ]
