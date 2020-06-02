# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helwan', '0002_auto_20180121_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='depart',
        ),
        migrations.AddField(
            model_name='profile',
            name='dep',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Computers'), (2, 'Communications')], null=True),
        ),
    ]
