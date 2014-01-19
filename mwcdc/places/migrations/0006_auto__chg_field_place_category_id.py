# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.category_id'
        db.alter_column(u'places_place', 'category_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Place.category_id'
        db.alter_column(u'places_place', 'category_id', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'category_label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'external_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hours': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'15211'", 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['places']