# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-25 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_apps', '0005_auto_20180625_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtrips',
            name='my_trips',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='first_apps.Registration'),
            preserve_default=False,
        ),
    ]
