# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0005_auto_20150402_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='link_title',
        ),
        migrations.AddField(
            model_name='feature',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feature',
            name='date_title',
            field=models.CharField(default=b'Release Date', max_length=128),
            preserve_default=True,
        ),
    ]
