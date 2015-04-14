# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0008_auto_20150408_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webcast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'GCIG Live', max_length=1024)),
                ('embed_identifier', models.CharField(max_length=2048, null=True, blank=True)),
                ('embed_type', models.CharField(max_length=20, choices=[(b'None', b'None'), (b'Basic iframe', b'iframe')])),
                ('disabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
