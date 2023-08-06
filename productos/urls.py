from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('login',views.ingresoUsuario,name='ingresoUsuario'),
    path('registroCursos',views.registroCursos,name='registroCursos'),
    path('eliminarCurso/<str:idCurso>',views.eliminarCursos,name='eliminarCurso'),
    path('asignarCurso',views.asignarCurso,name='asignarCurso'),
    path('verEstudiantes/<str:idCurso>',views.verEstudiantes,name='verEstudiantes')
]

#http://127.0.0.1:8000/productos/final