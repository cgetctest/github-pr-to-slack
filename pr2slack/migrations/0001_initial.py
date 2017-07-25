# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullReqeustThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.TextField()),
                ('thread', models.TextField()),
                ('repository', models.TextField()),
                ('pull_request', models.TextField()),
            ],
            options={
                'db_table': 'p2t_pull_reqeust_thread',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pullreqeustthread',
            unique_together=set([('repository', 'pull_request'), ('channel', 'thread')]),
        ),
    ]
