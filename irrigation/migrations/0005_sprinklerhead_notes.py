# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0004_drain_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprinklerhead',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
