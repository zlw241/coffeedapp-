# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 01:07
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151212_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_location),
        ),
    ]
