# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-11 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180411_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
