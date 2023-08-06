# Generated by Django 4.2.3 on 2023-08-06 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoproductos',
            name='direccionInfo',
        ),
        migrations.AddField(
            model_name='infoproductos',
            name='codigoProducto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.direccionusuario'),
        ),
        migrations.AddField(
            model_name='infoproductos',
            name='precioProducto',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
