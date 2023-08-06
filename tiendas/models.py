from django.db import models

# Create your models here.
class productoInfo(models.Model):
    nombreProducto = models.CharField(max_length=32, blank=True, null=True)
    apellidoProducto = models.CharField(max_length=32, blank=True, null=True)