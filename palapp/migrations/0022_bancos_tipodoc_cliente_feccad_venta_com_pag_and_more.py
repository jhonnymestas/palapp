# Generated by Django 4.0.5 on 2022-12-30 05:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0021_alter_cliente_fecact_alter_cliente_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rassoc', models.CharField(default='', max_length=80, unique=True, verbose_name='Razón Social')),
                ('activo', models.BooleanField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_act', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipodoc', models.CharField(default='', max_length=40, unique=True, verbose_name='Tipo DOcumento Sunat')),
                ('activo', models.BooleanField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_act', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='feccad',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha Caducidad'),
        ),
        migrations.AddField(
            model_name='venta',
            name='com_pag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venta',
            name='doc_pag_com',
            field=models.TextField(blank=True, default='', max_length=30, null=True, verbose_name='Documento Pago Comisión'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_pago_com',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Fecha Pago Comisión'),
        ),
        migrations.AddField(
            model_name='venta',
            name='foto_pago_com',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Foto Pago Comisión'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cel1',
            field=models.CharField(default='', max_length=15, unique=True, verbose_name='Celular 1'),
        ),
    ]