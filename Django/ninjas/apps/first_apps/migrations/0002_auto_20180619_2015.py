# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-19 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjas',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='first_apps.Dojo'),
        ),
    ]