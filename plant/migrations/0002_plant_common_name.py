# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='common_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]