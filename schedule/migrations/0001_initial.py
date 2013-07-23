# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'schedule_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('twitter_profile', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Speaker'])

        # Adding model 'Slot'
        db.create_table(u'schedule_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='talks', null=True, to=orm['schedule.Speaker'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Slot'])

        # Adding model 'Reference'
        db.create_table(u'schedule_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(related_name='references', to=orm['schedule.Slot'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'schedule', ['Reference'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'schedule_speaker')

        # Deleting model 'Slot'
        db.delete_table(u'schedule_slot')

        # Deleting model 'Reference'
        db.delete_table(u'schedule_reference')


    models = {
        u'schedule.reference': {
            'Meta': {'object_name': 'Reference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'references'", 'to': u"orm['schedule.Slot']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'schedule.slot': {
            'Meta': {'object_name': 'Slot'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'talks'", 'null': 'True', 'to': u"orm['schedule.Speaker']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'schedule.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_bio': ('django.db.models.fields.TextField', [], {}),
            'twitter_profile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']