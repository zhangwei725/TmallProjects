# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-26 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='110', max_length=11),
        ),
    ]