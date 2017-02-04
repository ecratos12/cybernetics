# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_libery_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olimp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Olimp_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=250)),
                ('result', models.TextField()),
                ('plase', models.CharField(max_length=250)),
                ('olimp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Olimp')),
            ],
        ),
    ]