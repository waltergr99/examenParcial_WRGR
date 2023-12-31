# Generated by Django 4.2.3 on 2023-08-06 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_infoproductos_direccioninfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoproductos',
            name='codigoProductointerno',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.direccionusuario'),
        ),
        migrations.AlterField(
            model_name='infoproductos',
            name='codigoProducto',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
