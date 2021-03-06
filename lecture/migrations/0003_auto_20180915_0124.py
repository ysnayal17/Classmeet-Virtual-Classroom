# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-15 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecture', '0002_auto_20180914_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='video',
            name='file_type',
        ),
        migrations.AddField(
            model_name='coursepack',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coursepack',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pdf',
            name='pdf_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='podcast',
            name='podcast_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='coursepack',
            name='thumbnail',
            field=models.FileField(upload_to=''),
        ),
    ]
