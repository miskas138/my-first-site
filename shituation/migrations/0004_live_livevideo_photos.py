# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shituation', '0003_song_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='LiveVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('live', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shituation.Live')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('live', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shituation.Live')),
            ],
        ),
    ]
