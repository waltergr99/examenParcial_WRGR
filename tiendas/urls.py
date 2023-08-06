from django.urls import path
from . import views

app_name = 'tiendas'
urlpatterns = [
    path('',views.index,name='index'),
    path('pucp-django',views.ejemplo,name='ejemplo'),
    path('cetam-django',views.cetam,name='cetam')
]