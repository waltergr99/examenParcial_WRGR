from django.db import models

# Create your models here.
class cursoInfo(models.Model):
    nombre = models.CharField(max_length=32, blank=True, null=True)
    direccion = models.CharField(max_length=32, blank=True, null=True)
    provincia = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    fechaInicio = models.CharField(max_length=32, blank=True, null=True)

class direccionUsuario(models.Model):
    ubicacion = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    
class infoProductos(models.Model):
    nombreProducto = models.CharField(max_length=32, blank=True, null=True)
    descripcionProducto = models.CharField(max_length=32, blank=True, null=True)
    codigoProductointerno = models.OneToOneField(direccionUsuario, on_delete=models.SET_NULL, blank=True, null=True)
    codigoProducto =models.CharField(max_length=32, blank=True, null=True)
    precioProducto =models.CharField(max_length=32, blank=True, null=True)
    cantidadProducto =models.CharField(max_length=32, blank=True, null=True)
    productoTienda = models.ForeignKey(cursoInfo,on_delete=models.SET_NULL,blank=True, null=True)
