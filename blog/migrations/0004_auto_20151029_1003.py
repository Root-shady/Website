# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151029_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(default='PL', choices=[('PL', 'Public'), ('PT', 'Private'), ('RT', 'Reprint'), ('DE', 'Debatable')], max_length=2),
        ),
    ]
