# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0003_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='disable',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
