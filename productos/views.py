from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import infoProductos , cursoInfo

# Create your views here.



def inicio(request):
    return HttpResponse('Bienvenidos a la aplicacion 2')

def ingresoProducto(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        codigoProducto = request.POST.get('codigoProducto'),
        precioProducto = request.POST.get('precioProducto'),
        cantidadProducto = request.POST.get('cantidadProducto')
        infoProductos.objects.create(
            nombreProducto=nombreProducto,
            descripcionProducto=descripcionProducto,
            codigoProducto=codigoProducto,
            precioProducto=precioProducto,
            cantidadProducto=cantidadProducto 
            )
        return HttpResponseRedirect(reverse('productos:ingresoProducto'))
    return render(request,'ingresoProducto.html',{
        'listaUsuarios':infoProductos.objects.all().order_by('id'),
    })

def registroTienda(request):
    usuarioSesion = infoProductos.objects.get(id=2)
    if request.method == 'POST':
        nombreCurso = request.POST.get('nombreCurso')
        direccionCurso = request.POST.get('direccionCurso')
        provinciaCurso = request.POST.get('provinciaCurso')
        regionCurso = request.POST.get('regionCurso')
        fechaInicio = request.POST.get('fechaCurso')
        cursoInfo.objects.create(
            nombre=nombreCurso,
            direccionCurso=direccionCurso,
            provinciaCurso=provinciaCurso,
            regionCurso=regionCurso,
            fechaInicio=fechaInicio
        )
        return HttpResponseRedirect(reverse('productos:registroTienda'))
    return render(request,'registroTienda.html',{
        'usuarioSession':usuarioSesion,
        'cursosTotales':cursoInfo.objects.all().order_by('id'),
        'usuariosTotales':infoProductos.objects.all().order_by('id')
    })


def eliminarCursos(request,idCurso):
    cursoEliminar = cursoInfo.objects.get(id=idCurso) 
    cursoEliminar.delete()
    return HttpResponseRedirect(reverse('productos:registroTienda')) 

def asignarCurso(request):
    if request.method == 'POST':
        idUsuario = request.POST.get('usuarioSeleccionado')
        idCurso = request.POST.get('cursoSeleccionado')
        objetoUsuario = infoProductos.objects.get(id=idUsuario)
        objectoCurso = cursoInfo.objects.get(id=idCurso)
        objetoUsuario.productoTienda = objectoCurso 
        objetoUsuario.save()
    return HttpResponseRedirect(reverse('productos:registroTienda'))

def verEstudiantes(request,idCurso):
    #cursoSeleccionado = cursoInfo.objects.get(id=idCurso)
    #estudiantesCurso = cursoSeleccionado.infoProductos_set.all().order_by('id')
    #for estudianteInfo in estudiantesCurso:
     #   print(f"{estudianteInfo.nombreProducto}{estudianteInfo.descripcionProducto}")
    return HttpResponseRedirect(reverse('productos:registroTienda'))