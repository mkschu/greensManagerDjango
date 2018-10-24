# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-14 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_tee_notes'),
        ('aerating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuadraTining',
            fields=[
                ('aerating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aerating.Aerating')),
                ('green', models.ManyToManyField(to='courses.Green')),
            ],
            bases=('aerating.aerating',),
        ),
    ]
