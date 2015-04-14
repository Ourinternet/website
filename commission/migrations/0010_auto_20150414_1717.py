# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0009_webcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=1024, null=True, blank=True)),
                ('link_title', models.CharField(max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderedFeatureLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('feature', models.ForeignKey(to='commission.Feature')),
                ('link', models.ForeignKey(to='commission.FeatureLink')),
            ],
            options={
                'ordering': ('feature', 'weight'),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='feature',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='button_link_title',
        ),
        migrations.AddField(
            model_name='feature',
            name='feature_links',
            field=models.ManyToManyField(to='commission.FeatureLink', null=True, through='commission.OrderedFeatureLink', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='webcast',
            name='embed_type',
            field=models.CharField(max_length=20, choices=[(b'None', b'None'), (b'iframe', b'Basic iframe')]),
        ),
    ]
