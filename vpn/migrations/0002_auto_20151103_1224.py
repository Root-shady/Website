# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128),
        ),
    ]
