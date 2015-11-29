# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPnumber',
            fields=[
                ('qihao', models.IntegerField(serialize=False, primary_key=True)),
                ('shuzi', models.CharField(max_length=7)),
                ('wan', models.IntegerField(default=-1)),
                ('qian', models.IntegerField(default=-1)),
                ('bai', models.IntegerField(default=-1)),
                ('shi', models.IntegerField(default=-1)),
                ('ge', models.IntegerField(default=-1)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2015, 11, 28, 6, 53, 50, 65126, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='CPUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=16)),
                ('url', models.CharField(max_length=300)),
                ('used', models.BooleanField(default=True)),
            ],
        ),
    ]
