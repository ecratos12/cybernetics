# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_schedule_block_up_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
    ]
