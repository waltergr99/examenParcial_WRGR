from django.db import models

# Create your models here.
class cursoInfo(models.Model):
    nombre = models.CharField(max_length=32, blank=True, null=True)
    fechaInicio = models.CharField(max_length=32, blank=True, null=True)

class direccionUsuario(models.Model):
    ubicacion = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    
class infoUsuarios(models.Model):
    nombreUsuario = models.CharField(max_length=32, blank=True, null=True)
    apellidoUsuario = models.CharField(max_length=32, blank=True, null=True)
    nroCelular =models.CharField(max_length=32, blank=True, null=True)
    direccionInfo = models.OneToOneField(direccionUsuario, on_delete=models.SET_NULL, blank=True, null=True)
    cursoUsuario = models.ForeignKey(cursoInfo,on_delete=models.SET_NULL,blank=True, null=True)
