# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-04 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cultinadb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menue',
            old_name='step_1',
            new_name='schritte_1',
        ),
        migrations.RenameField(
            model_name='menue',
            old_name='step_2',
            new_name='schritte_2',
        ),
        migrations.RenameField(
            model_name='menue',
            old_name='step_3',
            new_name='schritte_3',
        ),
        migrations.RenameField(
            model_name='menue',
            old_name='step_4',
            new_name='schritte_4',
        ),
    ]
