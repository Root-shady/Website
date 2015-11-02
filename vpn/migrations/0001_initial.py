# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=1, blank=True, default='F')),
                ('joined_date', models.DateTimeField(editable=False)),
                ('last_login', models.DateTimeField()),
                ('user_level', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
