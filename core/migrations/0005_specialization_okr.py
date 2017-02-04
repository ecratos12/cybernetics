# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_specialization_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='okr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.OKR'),
        ),
    ]