# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-07 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stimping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stimp',
            name='adj_speed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='backward1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='backward2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='backward3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='backwardAvg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='forward1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='forward2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='forward3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='forwardAvg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='left1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='left2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='left3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='leftAvg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='mu_k',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='raw_speed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='right1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='right2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='right3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='rightAvg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stimp',
            name='stdDev',
            field=models.FloatField(),
        ),
    ]
