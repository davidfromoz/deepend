# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0010_auto_20160418_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localplant',
            name='nitrogen_fixing',
        ),
        migrations.RemoveField(
            model_name='localplant',
            name='windbreak',
        ),
    ]
