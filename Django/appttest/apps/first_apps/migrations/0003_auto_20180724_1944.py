# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_apps', '0002_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='travel_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='travel_start',
            field=models.DateTimeField(),
        ),
    ]
