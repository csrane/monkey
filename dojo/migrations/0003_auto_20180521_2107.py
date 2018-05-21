# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_auto_20180521_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[dojo.models.min_length_3_validator]),
        ),
    ]
