# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-31 21:10
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicesettings',
            name='default_facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kolibriauth.Facility'),
        ),
    ]
