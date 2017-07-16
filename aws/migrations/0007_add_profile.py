# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-16 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0006_add_task_error'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='overrides',
        ),
        migrations.AddField(
            model_name='task',
            name='profile',
            field=models.CharField(max_length=100, null=True),
        ),
    ]