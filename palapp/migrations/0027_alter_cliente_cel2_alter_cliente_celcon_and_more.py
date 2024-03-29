# Generated by Django 4.0.5 on 2023-02-21 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0026_bancos_usuario_crea_tipodoc_usuario_crea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cel2',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Celular 2'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celcon',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Numero contacto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(default='AREQUIPA', null=True, verbose_name='Dirección Casa'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='directra',
            field=models.TextField(blank=True, default='AREQUIPA', null=True, verbose_name='Dirección Trabajo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(blank=True, default=' ', max_length=8, null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ocupacion',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Ocupación'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.CharField(default='PERU', max_length=50, null=True, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='percon',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Persona de contacto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telfij',
            field=models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Teléfono Fijo'),
        ),
        migrations.AlterField(
            model_name='tipodoc',
            name='tipodoc',
            field=models.CharField(default='', max_length=40, unique=True, verbose_name='Tipo Documento'),
        ),
    ]
