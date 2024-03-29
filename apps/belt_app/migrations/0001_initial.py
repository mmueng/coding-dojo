# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-24 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('other', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_job', to='login_app.User')),
                ('job_user', models.ManyToManyField(related_name='fav_movie', to='login_app.User')),
            ],
        ),
    ]
