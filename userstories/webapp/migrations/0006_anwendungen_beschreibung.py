# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-23 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_anwendungen_beschreibung'),
    ]

    operations = [
        migrations.AddField(
            model_name='anwendungen',
            name='beschreibung',
            field=models.TextField(blank=True, verbose_name='Beschreibung'),
        ),
    ]
