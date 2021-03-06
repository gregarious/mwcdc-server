# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table(u'skyline_interesetpointmapping', u'skyline_interestpointmapping')

    def backwards(self, orm):
        db.rename_table(u'skyline_interestpointmapping', u'skyline_interesetpointmapping')

    models = {
        u'skyline.interestpoint': {
            'Meta': {'object_name': 'InterestPoint'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'skyline.interestpointmapping': {
            'Meta': {'object_name': 'InterestPointMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skyline.InterestPoint']"}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skyline.Viewpoint']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'skyline.viewpoint': {
            'Meta': {'object_name': 'Viewpoint'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_points': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['skyline.InterestPoint']", 'through': u"orm['skyline.InterestPointMapping']", 'symmetrical': 'False'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skyline_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['skyline']