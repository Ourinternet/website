# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0012_video_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='date_title',
            field=models.CharField(default=b'Release Date', max_length=128, null=True, blank=True),
        ),
    ]
