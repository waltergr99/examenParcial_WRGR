from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('login',views.ingresoProducto,name='ingresoProducto'),
    path('registroTienda',views.registroTienda,name='registroTienda'),
    path('eliminarCurso/<str:idCurso>',views.eliminarCursos,name='eliminarCurso'),
    path('asignarCurso',views.asignarCurso,name='asignarCurso'),
    path('verEstudiantes/<str:idCurso>',views.verEstudiantes,name='verEstudiantes')
]

#http://127.0.0.1:8000/productos/final