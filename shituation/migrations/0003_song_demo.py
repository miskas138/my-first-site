# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shituation', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='demo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shituation.Demo'),
        ),
    ]
