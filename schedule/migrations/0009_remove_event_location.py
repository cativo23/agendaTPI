# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20171029_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]