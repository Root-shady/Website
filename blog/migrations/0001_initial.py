# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('abstract', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('status', models.CharField(default='Public', max_length=2, choices=[('Public', 'Public'), ('Private', 'Private'), ('Reprint', 'Reprint'), ('Debatable', 'Debatable')])),
                ('views', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relate_tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('frequence', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='relate_tag',
            name='tag',
            field=models.ForeignKey(to='blog.Tag'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='relate_tag',
            unique_together=set([('post', 'tag')]),
        ),
    ]
