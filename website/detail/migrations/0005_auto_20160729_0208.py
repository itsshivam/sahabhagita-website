# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0004_auto_20160729_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='email',
        ),
    ]
