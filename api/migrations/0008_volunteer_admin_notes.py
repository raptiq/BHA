# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-19 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_volunteer_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='admin_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
