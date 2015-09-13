# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCsv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('upload_file', models.FileField(upload_to=b'files/uploads/%Y/%m/%d')),
                ('city', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(default=b'1')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'uploadcsv',
            },
            bases=(models.Model,),
        ),
    ]
