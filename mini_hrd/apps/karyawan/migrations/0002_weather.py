# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_id', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('lar', models.CharField(max_length=100)),
                ('weather_state', models.CharField(max_length=100)),
            ],
        ),
    ]