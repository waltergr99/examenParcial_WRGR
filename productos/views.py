from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import infoUsuarios , cursoInfo

# Create your views here.



def inicio(request):
    return HttpResponse('Bienvenidos a la aplicacion 2')

def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        infoUsuarios.objects.create(
            nombreUsuario=nombreUsuario,
            apellidoUsuario=apellidoUsuario
            )
        return HttpResponseRedirect(reverse('productos:ingresoUsuario'))
    return render(request,'ingresoUsuario.html',{
        'listaUsuarios':infoUsuarios.objects.all().order_by('id'),
    })

def registroCursos(request):
    usuarioSesion = infoUsuarios.objects.get(id=2)
    if request.method == 'POST':
        nombreCurso = request.POST.get('nombreCurso')
        fechaInicio = request.POST.get('fechaCurso')
        cursoInfo.objects.create(
            nombre=nombreCurso,
            fechaInicio=fechaInicio
        )
        return HttpResponseRedirect(reverse('productos:registroCursos'))
    return render(request,'registroCursos.html',{
        'usuarioSession':usuarioSesion,
        'cursosTotales':cursoInfo.objects.all().order_by('id'),
        'usuariosTotales':infoUsuarios.objects.all().order_by('id')
    })


def eliminarCursos(request,idCurso):
    cursoEliminar = cursoInfo.objects.get(id=idCurso) 
    cursoEliminar.delete()
    return HttpResponseRedirect(reverse('productos:registroCursos')) 

def asignarCurso(request):
    if request.method == 'POST':
        idUsuario = request.POST.get('usuarioSeleccionado')
        idCurso = request.POST.get('cursoSeleccionado')
        objetoUsuario = infoUsuarios.objects.get(id=idUsuario)
        objectoCurso = cursoInfo.objects.get(id=idCurso)
        objetoUsuario.cursoUsuario = objectoCurso 
        objetoUsuario.save()
    return HttpResponseRedirect(reverse('productos:registroCursos'))

def verEstudiantes(request,idCurso):
    cursoSeleccionado = cursoInfo.objects.get(id=idCurso)
    estudiantesCurso = cursoSeleccionado.infousuarios_set.all().order_by('id')
    for estudianteInfo in estudiantesCurso:
        print(f"{estudianteInfo.nombreUsuario}{estudianteInfo.apellidoUsuario}")
    return HttpResponseRedirect(reverse('productos:registroCursos'))