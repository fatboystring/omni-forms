# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omniforms', '0019_auto_20180212_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmniChoiceField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('choices', models.TextField(help_text='Please add one choice per line.')),
            ],
            options={
                'verbose_name': 'Choice Field',
            },
            bases=('omniforms.omnifield', models.Model),
        ),
        migrations.CreateModel(
            name='OmniMultipleChoiceField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('choices', models.TextField(help_text='Please add one choice per line.')),
            ],
            options={
                'verbose_name': 'Multiple Choice Field',
            },
            bases=('omniforms.omnifield', models.Model),
        ),
    ]
