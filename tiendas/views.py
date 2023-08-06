from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a Django")

def ejemplo(request):
    return HttpResponse('Bienvenidos a la PUCP')

def cetam(request):
    return HttpResponse('Bienvenidos a cetam')