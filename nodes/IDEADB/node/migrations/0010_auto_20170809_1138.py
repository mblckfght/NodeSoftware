# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0009_auto_20170809_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='species',
            old_name='inchi',
            new_name='inchi_neutral',
        ),
    ]
