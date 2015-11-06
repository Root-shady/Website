# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0003_auto_20151106_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='joined_date',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
