# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 09:58
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161207_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.update_filename),
        ),
    ]