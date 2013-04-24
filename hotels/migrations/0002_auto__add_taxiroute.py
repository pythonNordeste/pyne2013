# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaxiRoute'
        db.create_table(u'hotels_taxiroute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hotels.Hotel'])),
            ('fr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('to', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('flag_1', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('flag_2', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'hotels', ['TaxiRoute'])


    def backwards(self, orm):
        # Deleting model 'TaxiRoute'
        db.delete_table(u'hotels_taxiroute')


    models = {
        u'hotels.bedroom': {
            'Meta': {'object_name': 'Bedroom'},
            'air_con': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotels.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_people': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_people': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'hotels.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bus_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hotel_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'hotels.taxiroute': {
            'Meta': {'object_name': 'TaxiRoute'},
            'flag_1': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'flag_2': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'fr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hotel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hotels.Hotel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['hotels']