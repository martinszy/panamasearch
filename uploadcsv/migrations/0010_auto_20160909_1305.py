# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsv', '0009_auto_20160903_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namelist',
            name='namefile',
            field=models.FileField(upload_to='data/jobs/'),
        ),
    ]