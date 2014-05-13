# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table(u'commission_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.PublicationType'])),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('document_link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'commission', ['Publication'])

        # Adding model 'PublicationType'
        db.create_table(u'commission_publicationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'commission', ['PublicationType'])

        # Adding model 'Author'
        db.create_table(u'commission_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('twitter_handle', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('short_bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('partner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.Partner'], null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'commission', ['Author'])

        # Adding model 'PublicationAuthor'
        db.create_table(u'commission_publicationauthor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.Publication'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.Author'])),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'commission', ['PublicationAuthor'])


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table(u'commission_publication')

        # Deleting model 'PublicationType'
        db.delete_table(u'commission_publicationtype')

        # Deleting model 'Author'
        db.delete_table(u'commission_author')

        # Deleting model 'PublicationAuthor'
        db.delete_table(u'commission_publicationauthor')


    models = {
        u'commission.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.Partner']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'commission.event': {
            'Meta': {'object_name': 'Event'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'commission.faq': {
            'Meta': {'object_name': 'FAQ'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'commission.mediacontact': {
            'Meta': {'object_name': 'MediaContact'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'display_on_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'commission.partner': {
            'Meta': {'object_name': 'Partner'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'press_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website_display': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'commission.pressreleasefooter': {
            'Meta': {'object_name': 'PressReleaseFooter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['commission.MediaContact']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['commission.Partner']", 'null': 'True', 'blank': 'True'})
        },
        u'commission.publication': {
            'Meta': {'object_name': 'Publication'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['commission.Author']", 'null': 'True', 'through': u"orm['commission.PublicationAuthor']", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'document_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.PublicationType']"})
        },
        u'commission.publicationauthor': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'PublicationAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.Author']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['commission.Publication']"}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'commission.publicationtype': {
            'Meta': {'object_name': 'PublicationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'commission.supporter': {
            'Meta': {'object_name': 'Supporter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['commission']