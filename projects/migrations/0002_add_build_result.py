# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-25 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='result',
            field=models.IntegerField(choices=[(0, 'Pending'), (10, 'Fail'), (19, 'Qualified pass'), (20, 'Pass')], default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(10, 'New'), (100, 'Active'), (1000, 'Attic'), (9999, 'Ignored')], default=10),
        ),
    ]