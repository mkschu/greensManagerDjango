# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20180328_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fluid',
            name='unit_size',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
