# Generated by Django 4.0.5 on 2022-09-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0010_alter_cliente_cel2_alter_cliente_celcon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='banco',
            field=models.TextField(blank=True, max_length=40, null=True, verbose_name='Banco'),
        ),
    ]
