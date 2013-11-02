# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Place.category'
        db.delete_column(u'places_place', 'category')

        # Deleting field 'Place.twitter_id'
        db.delete_column(u'places_place', 'twitter_id')

        # Deleting field 'Place.address'
        db.delete_column(u'places_place', 'address')

        # Adding field 'Place.street_address'
        db.add_column(u'places_place', 'street_address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Place.twitter_handle'
        db.add_column(u'places_place', 'twitter_handle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'Place.category_id'
        db.add_column(u'places_place', 'category_id',
                      self.gf('django.db.models.fields.IntegerField')(default=-1),
                      keep_default=False)

        # Adding field 'Place.category_label'
        db.add_column(u'places_place', 'category_label',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Place.category'
        db.add_column(u'places_place', 'category',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'Place.twitter_id'
        db.add_column(u'places_place', 'twitter_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Place.address'
        raise RuntimeError("Cannot reverse this migration. 'Place.address' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Place.address'
        db.add_column(u'places_place', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Deleting field 'Place.street_address'
        db.delete_column(u'places_place', 'street_address')

        # Deleting field 'Place.twitter_handle'
        db.delete_column(u'places_place', 'twitter_handle')

        # Deleting field 'Place.category_id'
        db.delete_column(u'places_place', 'category_id')

        # Deleting field 'Place.category_label'
        db.delete_column(u'places_place', 'category_label')


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
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'default': "'15211'", 'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['places']