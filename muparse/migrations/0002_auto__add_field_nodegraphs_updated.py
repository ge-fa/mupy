# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NodeGraphs.updated'
        db.add_column('muparse_nodegraphs', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 20, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NodeGraphs.updated'
        db.delete_column('muparse_nodegraphs', 'updated')


    models = {
        'muparse.graph': {
            'Meta': {'object_name': 'Graph'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muparse.GraphCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'muparse.graphcategory': {
            'Meta': {'object_name': 'GraphCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'muparse.node': {
            'Meta': {'object_name': 'Node'},
            'graphs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['muparse.Graph']", 'null': 'True', 'through': "orm['muparse.NodeGraphs']", 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muparse.NodeGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'muparse.nodegraphs': {
            'Meta': {'object_name': 'NodeGraphs'},
            'baseurl': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muparse.Graph']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['muparse.Node']"}),
            'pageurl': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'muparse.nodegroup': {
            'Meta': {'object_name': 'NodeGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'muparse.savedsearch': {
            'Meta': {'object_name': 'SavedSearch'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'graphs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['muparse.NodeGraphs']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['muparse']