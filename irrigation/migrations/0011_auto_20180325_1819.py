# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0010_auto_20180228_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprinklerhead',
            name='make',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='sprinklerhead',
            name='model',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]