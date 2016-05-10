# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0004_plant_windbreak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=20)),
                ('tagcolor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='plants',
            field=models.ManyToManyField(to='plant.Plant'),
        ),
    ]
