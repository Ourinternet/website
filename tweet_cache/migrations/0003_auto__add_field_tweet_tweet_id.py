# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Tweet.tweet_id'
        db.add_column(u'tweet_cache_tweet', 'tweet_id',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Tweet.tweet_id'
        db.delete_column(u'tweet_cache_tweet', 'tweet_id')


    models = {
        u'tweet_cache.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed_text': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tweet_id': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['tweet_cache']