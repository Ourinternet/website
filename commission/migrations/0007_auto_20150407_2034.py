# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0006_auto_20150407_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='link',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
    ]
