# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omniforms', '0018_auto_20180212_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='omnibooleanfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnicharfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnidatefield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnidatetimefield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnidecimalfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnidurationfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omniemailfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnifloatfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnigenericipaddressfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omniintegerfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnislugfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omnitimefield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omniurlfield',
            old_name='initial',
            new_name='initial_data',
        ),
        migrations.RenameField(
            model_name='omniuuidfield',
            old_name='initial',
            new_name='initial_data',
        ),
    ]
