# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0010_auto_20150414_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurelink',
            name='icon',
            field=models.CharField(default=b'fa-mail-forward', max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
    ]
