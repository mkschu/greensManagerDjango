# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0004_timeunit'),
        ('fertilizing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fertilizer',
            name='bag_units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='measures.Unit'),
        ),
    ]
