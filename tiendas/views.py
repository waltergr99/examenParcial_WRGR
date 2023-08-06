from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import productoInfo

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a Django")

def ejemplo(request):
    return HttpResponse('Bienvenidos a la PUCP')

def cetam(request):
    return HttpResponse('Bienvenidos a cetam')

def eliminarProducto(request,idTienda):
    cursoEliminar = productoInfo.objects.get(id=idTienda) 
    cursoEliminar.delete()
    return HttpResponseRedirect(reverse('productos:ingresoProducto')) 
