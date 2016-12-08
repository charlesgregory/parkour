# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0019_sample_is_converted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('size', models.PositiveIntegerField(blank=True, default=0, verbose_name='Pool Size')),
            ],
        ),
        migrations.CreateModel(
            name='PoolFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pools/%Y/%m/%d/')),
            ],
        ),
        migrations.AddField(
            model_name='pool',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index_generator.PoolFile', verbose_name='File'),
        ),
        migrations.AddField(
            model_name='pool',
            name='libraries',
            field=models.ManyToManyField(blank=True, to='library.Library'),
        ),
        migrations.AddField(
            model_name='pool',
            name='samples',
            field=models.ManyToManyField(blank=True, to='library.Sample'),
        ),
    ]
