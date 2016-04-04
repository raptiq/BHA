# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-04 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160403_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('start_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('contact', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Contact')),
                ('language', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Language')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posted_assignments', to='api.Volunteer')),
                ('volunteers', models.ManyToManyField(blank=True, related_name='assignments', to='api.Volunteer')),
            ],
        ),
    ]