# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machines', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mow_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FairwayMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('fairway', models.ManyToManyField(to='courses.Fairway')),
                ('mower', models.ManyToManyField(to='machines.FairwayMower')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='GreensMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('green', models.ManyToManyField(to='courses.Green')),
                ('mower', models.ManyToManyField(to='machines.GreensMower')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='RoughMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('mower', models.ManyToManyField(to='machines.RoughMower')),
                ('rough', models.ManyToManyField(to='courses.Rough')),
            ],
            bases=('mowing.mowing',),
        ),
        migrations.CreateModel(
            name='TeeMowing',
            fields=[
                ('mowing_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mowing.Mowing')),
                ('mower', models.ManyToManyField(to='machines.TeeMower')),
                ('tee', models.ManyToManyField(to='courses.Tee')),
            ],
            bases=('mowing.mowing',),
        ),
    ]
