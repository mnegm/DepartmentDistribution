# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helwan', '0006_auto_20180129_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='deg',
            new_name='Degree',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='dep',
            new_name='Department',
        ),
    ]