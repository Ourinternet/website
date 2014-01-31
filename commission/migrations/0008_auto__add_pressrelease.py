# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MediaContact'
        db.create_table(u'commission_mediacontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'commission', ['MediaContact'])

        # Adding model 'PressReleaseFooter'
        db.create_table(u'commission_pressreleasefooter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'commission', ['PressReleaseFooter'])

        # Adding M2M table for field media_contacts on 'PressReleaseFooter'
        m2m_table_name = db.shorten_name(u'commission_pressreleasefooter_media_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pressreleasefooter', models.ForeignKey(orm[u'commission.pressreleasefooter'], null=False)),
            ('mediacontact', models.ForeignKey(orm[u'commission.mediacontact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pressreleasefooter_id', 'mediacontact_id'])

        # Adding M2M table for field partners on 'PressReleaseFooter'
        m2m_table_name = db.shorten_name(u'commission_pressreleasefooter_partners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pressreleasefooter', models.ForeignKey(orm[u'commission.pressreleasefooter'], null=False)),
            ('partner', models.ForeignKey(orm[u'commission.partner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pressreleasefooter_id', 'partner_id'])

        # Adding model 'PressRelease'
        db.create_table(u'commission_pressrelease', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('footer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commission.PressReleaseFooter'], null=True, blank=True)),
            ('release_tag', self.gf('django.db.models.fields.TextField')(default='For immediate release')),
            ('end_tag', self.gf('django.db.models.fields.CharField')(default='-30-', max_length=20)),
        ))
        db.send_create_signal(u'commission', ['PressRelease'])

        # Adding field 'Partner.short_name'
        db.add_column(u'commission_partner', 'short_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Partner.website'
        db.add_column(u'commission_partner', 'website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Partner.description'
        db.add_column(u'commission_partner', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Partner.press_description'
        db.add_column(u'commission_partner', 'press_description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'MediaContact'
        db.delete_table(u'commission_mediacontact')

        # Deleting model 'PressReleaseFooter'
        db.delete_table(u'commission_pressreleasefooter')

        # Removing M2M table for field media_contacts on 'PressReleaseFooter'
        db.delete_table(db.shorten_name(u'commission_pressreleasefooter_media_contacts'))

        # Removing M2M table for field partners on 'PressReleaseFooter'
        db.delete_table(db.shorten_name(u'commission_pressreleasefooter_partners'))

        # Deleting model 'PressRelease'
        db.delete_table(u'commission_pressrelease')

        # Deleting field 'Partner.short_name'
        db.delete_column(u'commission_partner', 'short_name')

        # Deleting field 'Partner.website'
        db.delete_column(u'commission_partner', 'website')

        # Deleting field 'Partner.description'
        db.delete_column(u'commission_partner', 'description')

        # Deleting field 'Partner.press_description'
        db.delete_column(u'commission_partner', 'press_description')


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