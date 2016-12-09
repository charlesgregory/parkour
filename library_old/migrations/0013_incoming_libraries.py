# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_filelibrary_filesample'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='amount_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='library',
            name='barcode',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Barcode'),
        ),
        migrations.AddField(
            model_name='library',
            name='comments_facility',
            field=models.TextField(blank=True, null=True, verbose_name='Comments (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='concentration_determined_by_facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='library.ConcentrationMethod', verbose_name='Concentration Determined by (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='concentration_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='Concentration (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='date_facility',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='dilution_factor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dilution Factor'),
        ),
        migrations.AddField(
            model_name='library',
            name='is_in_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='library',
            name='qc_result',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='QC Result'),
        ),
        migrations.AddField(
            model_name='library',
            name='qpcr_result_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='qPCR Result (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='sample_volume_facility',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sample Volume (facility)'),
        ),
        migrations.AddField(
            model_name='library',
            name='size_distribution_facility',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Size Distribution'),
        ),
        migrations.AddField(
            model_name='sample',
            name='amount_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='sample',
            name='barcode',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Barcode'),
        ),
        migrations.AddField(
            model_name='sample',
            name='comments_facility',
            field=models.TextField(blank=True, null=True, verbose_name='Comments (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='concentration_determined_by_facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='library.ConcentrationMethod', verbose_name='Concentration Determined by (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='concentration_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='Concentration (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='date_facility',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='dilution_factor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dilution Factor'),
        ),
        migrations.AddField(
            model_name='sample',
            name='is_in_request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sample',
            name='qc_result',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='QC Result'),
        ),
        migrations.AddField(
            model_name='sample',
            name='rna_quality_facility',
            field=models.FloatField(blank=True, null=True, verbose_name='RNA Quality (RIN, RQN) (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_volume_facility',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sample Volume (facility)'),
        ),
        migrations.AddField(
            model_name='sample',
            name='size_distribution_facility',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Size Distribution'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='amplified_cycles',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sample Amplified Cycles'),
        ),
    ]