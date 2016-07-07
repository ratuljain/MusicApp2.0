# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=50)),
                ('cover_image_url', models.CharField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.Genre')),
            ],
        ),
    ]