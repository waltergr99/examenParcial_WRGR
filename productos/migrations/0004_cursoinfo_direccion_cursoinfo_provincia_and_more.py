# Generated by Django 4.2.3 on 2023-08-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_infoproductos_codigoproductointerno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursoinfo',
            name='direccion',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='cursoinfo',
            name='provincia',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='cursoinfo',
            name='region',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
