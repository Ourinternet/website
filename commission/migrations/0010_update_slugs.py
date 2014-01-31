# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.utils.text import slugify

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        press_releases = orm.PressRelease.objects.all()
        for release in press_releases:
            release.slug = slugify(release.title)
            release.save()


    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'commission.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'commission.mediacontact': {
            'Meta': {'object_name': 'MediaContact'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'commission.member': {
            'Meta': {'object_name': 'Member'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'member_type': ('django.db.models.fields.CharField', [], {'default': "'general'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.Partner']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'commission.partner': {
            'Meta': {'object_name': 'Partner'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'press_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'commission.pressrelease': {
            'Meta': {'object_name': 'PressRelease'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_tag': ('django.db.models.fields.CharField', [], {'default': "'-30-'", 'max_length': '20'}),
            'footer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.PressReleaseFooter']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {}),
            'release_tag': ('django.db.models.fields.TextField', [], {'default': "'For immediate release'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '1024'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'commission.pressreleasefooter': {
            'Meta': {'object_name': 'PressReleaseFooter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['commission.MediaContact']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['commission.Partner']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['commission']
    symmetrical = True
