# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0004_feature_disable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feature',
            options={'ordering': ('weight',)},
        ),
        migrations.AddField(
            model_name='feature',
            name='weight',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
