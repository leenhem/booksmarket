# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-11 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180411_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blo',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Blo',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
