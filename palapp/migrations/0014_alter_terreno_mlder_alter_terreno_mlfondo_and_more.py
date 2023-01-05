# Generated by Django 4.0.5 on 2022-09-15 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0013_alter_venta_condvta_alter_venta_nro_cont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreno',
            name='mlder',
            field=models.TextField(default='', null=True, verbose_name='Mts Lin. Derecha'),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='mlfondo',
            field=models.TextField(default='', null=True, verbose_name='Mts Lin. Fondo'),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='mlfrente',
            field=models.TextField(default='', null=True, verbose_name='Mts Lin. de Frente'),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='mlizq',
            field=models.TextField(default='', null=True, verbose_name='Mts Lin. Izquierda'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='terreno',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='palapp.terreno', unique=True, verbose_name='Terreno'),
        ),
    ]