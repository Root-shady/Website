# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151029_1003'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relate_tag',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='relate_tag',
            name='post',
        ),
        migrations.RemoveField(
            model_name='relate_tag',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.DeleteModel(
            name='Relate_tag',
        ),
    ]
