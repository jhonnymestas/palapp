# Generated by Django 4.0.5 on 2022-09-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0007_pagos_efectivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notaria',
            old_name='ressoc',
            new_name='rassoc',
        ),
    ]
