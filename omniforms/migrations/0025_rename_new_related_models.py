# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 06:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omniforms', '0024_delete_old_related_models'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OmniForeignKeyFieldNew',
            new_name='OmniForeignKeyField',
        ),
        migrations.RenameModel(
            old_name='OmniManyToManyFieldNew',
            new_name='OmniManyToManyField',
        ),
    ]
