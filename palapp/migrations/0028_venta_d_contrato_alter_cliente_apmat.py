# Generated by Django 4.1.7 on 2023-03-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0027_alter_cliente_cel2_alter_cliente_celcon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='d_contrato',
            field=models.FileField(blank=True, default='', upload_to='media/', verbose_name='Doc.Escaneado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apmat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno'),
        ),
    ]
