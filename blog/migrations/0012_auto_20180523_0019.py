# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
