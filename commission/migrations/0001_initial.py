# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=512, null=True, blank=True)),
                ('twitter_handle', models.CharField(max_length=60, null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True)),
                ('website', models.CharField(max_length=256, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('company', models.CharField(max_length=256)),
                ('telephone', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=256)),
                ('display_on_contact', models.BooleanField(default=True)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=512, null=True, blank=True)),
                ('twitter_handle', models.CharField(max_length=60, null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True)),
                ('website', models.CharField(max_length=256, null=True, blank=True)),
                ('member_type', models.CharField(default=b'general', max_length=20, choices=[(b'chair', b'chair'), (b'general', b'general'), (b'supporting', b'supporting'), (b'research_adviser', b'research adviser')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('short_name', models.CharField(max_length=30, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('website_display', models.CharField(max_length=256, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('press_description', models.TextField(null=True, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'partner_logos', blank=True)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('release_date', models.DateTimeField()),
                ('location', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('release_tag', models.TextField(default=b'For immediate release')),
                ('end_tag', models.CharField(default=b'-30-', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PressReleaseFooter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('media_contacts', models.ManyToManyField(to='commission.MediaContact', null=True, blank=True)),
                ('partners', models.ManyToManyField(to='commission.Partner', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('publish_date', models.DateField()),
                ('document', models.FileField(null=True, upload_to=b'publications', blank=True)),
                ('document_link', models.URLField(null=True, blank=True)),
                ('document_link_title', models.CharField(default=b'Download PDF', max_length=128)),
                ('image', models.ImageField(null=True, upload_to=b'publications/images', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicationAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(related_name=b'ordered_authors', to='commission.Author')),
                ('publication', models.ForeignKey(to='commission.Publication')),
            ],
            options={
                'ordering': ('weight',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('website', models.URLField(null=True, blank=True)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('video_id', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('weight', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(to='commission.Author', null=True, through='commission.PublicationAuthor', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.ForeignKey(to='commission.PublicationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pressrelease',
            name='footer',
            field=models.ForeignKey(blank=True, to='commission.PressReleaseFooter', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='partner',
            field=models.ForeignKey(blank=True, to='commission.Partner', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='partner',
            field=models.ForeignKey(blank=True, to='commission.Partner', null=True),
            preserve_default=True,
        ),
    ]
