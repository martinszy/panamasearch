# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsv', '0003_auto_20160827_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namelist',
            name='textlist',
            field=models.TextField(blank=True, null=True),
        ),
    ]