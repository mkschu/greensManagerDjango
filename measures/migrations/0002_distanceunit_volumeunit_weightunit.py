# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceUnit',
            fields=[
                ('unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measures.Unit')),
                ('conversion', models.FloatField()),
            ],
            bases=('measures.unit',),
        ),
        migrations.CreateModel(
            name='VolumeUnit',
            fields=[
                ('unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measures.Unit')),
                ('conversion', models.FloatField()),
            ],
            bases=('measures.unit',),
        ),
        migrations.CreateModel(
            name='WeightUnit',
            fields=[
                ('unit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='measures.Unit')),
                ('conversion', models.FloatField()),
            ],
            bases=('measures.unit',),
        ),
    ]
