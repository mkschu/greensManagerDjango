# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0004_timeunit'),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oilchange',
            name='oil_units',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measures.VolumeUnit'),
            preserve_default=False,
        ),
    ]
