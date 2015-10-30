# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151029_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('category', 'publish_date')},
        ),
        migrations.AddField(
            model_name='category',
            name='related_post',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
