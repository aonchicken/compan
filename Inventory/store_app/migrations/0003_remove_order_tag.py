# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-07 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_auto_20180607_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
    ]
