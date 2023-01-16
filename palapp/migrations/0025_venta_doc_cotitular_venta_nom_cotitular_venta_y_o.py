# Generated by Django 4.0.5 on 2023-01-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0024_venta_bco_pag_com_venta_tdoc_sun_com_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='doc_cotitular',
            field=models.TextField(blank=True, default='', max_length=30, null=True, verbose_name='Documento Cotitular'),
        ),
        migrations.AddField(
            model_name='venta',
            name='nom_cotitular',
            field=models.TextField(blank=True, default='', max_length=80, null=True, verbose_name='Cotitular'),
        ),
        migrations.AddField(
            model_name='venta',
            name='y_o',
            field=models.TextField(blank=True, default='', max_length=1, null=True, verbose_name='Y/O'),
        ),
    ]