# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article_nav_bar'),
    ]

    operations = [
        migrations.CreateModel(
            name='OKR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]