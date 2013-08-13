# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InterestPoint'
        db.create_table(u'skyline_interestpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'skyline', ['InterestPoint'])

        # Adding model 'Viewpoint'
        db.create_table(u'skyline_viewpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=6)),
            ('skyline_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'skyline', ['Viewpoint'])

        # Adding model 'InteresetPointMapping'
        db.create_table(u'skyline_interesetpointmapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interest_point', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skyline.InterestPoint'])),
            ('viewpoint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skyline.Viewpoint'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'skyline', ['InteresetPointMapping'])


    def backwards(self, orm):
        # Deleting model 'InterestPoint'
        db.delete_table(u'skyline_interestpoint')

        # Deleting model 'Viewpoint'
        db.delete_table(u'skyline_viewpoint')

        # Deleting model 'InteresetPointMapping'
        db.delete_table(u'skyline_interesetpointmapping')


    models = {
        u'skyline.interesetpointmapping': {
            'Meta': {'object_name': 'InteresetPointMapping'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skyline.InterestPoint']"}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'viewpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skyline.Viewpoint']"}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        u'skyline.interestpoint': {
            'Meta': {'object_name': 'InterestPoint'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'skyline.viewpoint': {
            'Meta': {'object_name': 'Viewpoint'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest_points': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['skyline.InterestPoint']", 'through': u"orm['skyline.InteresetPointMapping']", 'symmetrical': 'False'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skyline_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['skyline']