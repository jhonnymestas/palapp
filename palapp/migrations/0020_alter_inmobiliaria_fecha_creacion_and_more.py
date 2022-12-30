# Generated by Django 4.0.5 on 2022-12-18 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0019_alter_inmobiliaria_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmobiliaria',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inmobiliaria',
            name='fecha_inicon',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 18, 23, 40, 50849, tzinfo=utc), verbose_name='Fecha Inicio de Contrato'),
        ),
    ]
