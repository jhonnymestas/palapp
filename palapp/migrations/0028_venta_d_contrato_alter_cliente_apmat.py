# Generated by Django 4.0.5 on 2023-02-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palapp', '0027_alter_cliente_cel2_alter_cliente_celcon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='d_contrato',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apmat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido Materno'),
        ),
    ]
