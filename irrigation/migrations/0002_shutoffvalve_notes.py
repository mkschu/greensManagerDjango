# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shutoffvalve',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]