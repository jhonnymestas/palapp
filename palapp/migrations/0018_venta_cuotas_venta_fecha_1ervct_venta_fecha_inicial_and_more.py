# Generated by Django 4.0.5 on 2022-11-11 05:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0017_alter_inmobiliaria_fecha_act_alter_pagos_venta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cuotas',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='No.Cuotas'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_1ervct',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_inicial',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Fecha entrega Inicial'),
        ),
        migrations.AddField(
            model_name='venta',
            name='inicial',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Inicial US$'),
        ),
    ]
