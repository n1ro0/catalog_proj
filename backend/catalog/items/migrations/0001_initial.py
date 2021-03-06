# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 07:59
from __future__ import unicode_literals

import catalog.items.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=300)),
                ('price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='items/default.png', upload_to=catalog.items.models.upload_to)),
                ('categories', models.ManyToManyField(related_name='items', to='categories.Category')),
            ],
            options={
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
