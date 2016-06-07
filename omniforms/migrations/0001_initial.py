# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import omniforms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmniField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('required', models.BooleanField(default=False)),
                ('widget_class', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='OmniForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(omniforms.models.FormGeneratorMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OmniFormHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='OmniModelForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(help_text='THis is some help text', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(omniforms.models.FormGeneratorMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OmniBooleanField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.NullBooleanField()),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniCharField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.TextField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniDateField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.DateField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniDateTimeField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniDecimalField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniEmailField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniFloatField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.FloatField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniFormEmailHandler',
            fields=[
                ('omniformhandler_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniFormHandler')),
                ('subject', models.CharField(max_length=255)),
                ('recipients', models.TextField()),
                ('template', models.TextField()),
            ],
            bases=('omniforms.omniformhandler',),
        ),
        migrations.CreateModel(
            name='OmniIntegerField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.IntegerField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniRelatedField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniTimeField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.TimeField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.CreateModel(
            name='OmniUrlField',
            fields=[
                ('omnifield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniField')),
                ('initial', models.URLField(blank=True, null=True)),
            ],
            bases=('omniforms.omnifield',),
        ),
        migrations.AddField(
            model_name='omniformhandler',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='omniformhandler',
            name='real_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='omnifield',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='omnifield',
            name='real_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
        migrations.CreateModel(
            name='OmniForeignKeyField',
            fields=[
                ('omnirelatedfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniRelatedField')),
            ],
            bases=('omniforms.omnirelatedfield',),
        ),
        migrations.CreateModel(
            name='OmniManyToManyField',
            fields=[
                ('omnirelatedfield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='omniforms.OmniRelatedField')),
            ],
            bases=('omniforms.omnirelatedfield',),
        ),
        migrations.AddField(
            model_name='omnirelatedfield',
            name='related_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType'),
        ),
    ]
