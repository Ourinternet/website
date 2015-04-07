# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0002_publication_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_line', models.CharField(max_length=1024, null=True, blank=True)),
                ('title', models.CharField(max_length=1024, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('link_title', models.CharField(default=b'View', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
