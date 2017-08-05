# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-05 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cultinadb', '0004_auto_20170805_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menue',
            name='type_of_dish_quantity',
            field=models.CharField(blank=True, choices=[('Gericht', 'Gericht'), ('Suppe', 'Suppe'), ('Dessert', 'Dessert'), ('...', '...')], max_length=2, verbose_name='Art der Nahrung'),
        ),
        migrations.AlterField(
            model_name='menue',
            name='zutaten',
            field=wagtail.wagtailcore.fields.StreamField((('zutaten', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='cultinadb.ingredients')),), blank=True, null=True),
        ),
    ]
