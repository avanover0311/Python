# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-27 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_apps', '0002_auto_20180727_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
