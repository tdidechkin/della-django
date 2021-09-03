# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 12:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='santee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='santa', to=settings.AUTH_USER_MODEL),
        ),
    ]
