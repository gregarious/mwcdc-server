# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.longitude'
        db.alter_column(u'places_place', 'longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6))

        # Changing field 'Place.latitude'
        db.alter_column(u'places_place', 'latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Place.longitude'
        raise RuntimeError("Cannot reverse this migration. 'Place.longitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Place.longitude'
        db.alter_column(u'places_place', 'longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6))

        # User chose to not deal with backwards NULL issues for 'Place.latitude'
        raise RuntimeError("Cannot reverse this migration. 'Place.latitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Place.latitude'
        db.alter_column(u'places_place', 'latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6))

    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'category_label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hours': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'15211'", 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['places']