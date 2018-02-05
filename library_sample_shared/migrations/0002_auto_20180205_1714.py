# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-05 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_sample_shared', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barcodecounter',
            name='counter',
        ),
        migrations.AddField(
            model_name='barcodecounter',
            name='last_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barcodecounter',
            name='year',
            field=models.PositiveSmallIntegerField(default=2018, unique=True),
        ),
    ]