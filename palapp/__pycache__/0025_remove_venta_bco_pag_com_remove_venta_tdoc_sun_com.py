# Generated by Django 4.0.5 on 2022-12-30 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0024_alter_venta_bco_pag_com_alter_venta_tdoc_sun_com'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='bco_pag_com',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='tdoc_sun_com',
        ),
    ]