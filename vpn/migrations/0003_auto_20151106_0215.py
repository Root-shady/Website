# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vpn', '0002_auto_20151103_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sex', models.CharField(max_length=1, choices=[('F', 'female'), ('M', 'male')], blank=True)),
                ('joined_date', models.DateTimeField(editable=False)),
                ('last_login', models.DateTimeField()),
                ('user_level', models.PositiveIntegerField(default=0)),
                ('status', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
