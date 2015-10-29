# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('post_id', 'publish_date')},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
