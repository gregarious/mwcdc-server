# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'places_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hours', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('twitter_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(default='15211', max_length=10)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'places', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'places_place')


    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hours': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'15211'", 'max_length': '10'})
        }
    }

    complete_apps = ['places']