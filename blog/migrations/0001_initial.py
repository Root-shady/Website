# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('related_post', models.PositiveIntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('abstract', models.CharField(max_length=300)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=2, default='PL', choices=[('PL', 'Public'), ('PT', 'Private'), ('RT', 'Reprint'), ('DE', 'Debatable')])),
                ('views', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('frequence', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
