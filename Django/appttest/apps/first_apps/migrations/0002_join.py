# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-23 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_trips', to='first_apps.Trips')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_trips', to='first_apps.User')),
            ],
        ),
    ]
