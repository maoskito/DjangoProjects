# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test_field',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
