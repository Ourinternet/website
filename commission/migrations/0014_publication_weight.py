# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0013_auto_20150513_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='weight',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
