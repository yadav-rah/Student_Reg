# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-06 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0002_auto_20180106_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studmarks',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='studapp.Student', unique=True),
        ),
    ]