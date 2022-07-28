from calendar import calendar
from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola mundo")

def pan(request):
    return HttpResponse("Pan de muerto")

def dia(request):
    hoy = datetime.today()
    return HttpResponse(f'El dia de hoy es {hoy.strftime("%A, %d de %B de %Y")}')

def saludo_nombre(request, nombre):
    return HttpResponse(f'Hola {nombre}')

def fecha_nacimiento(request, anio):
    calEdad = datetime.today().year - int(anio)
    return HttpResponse(f'Tu año de nacimiento fue el {calEdad}')

def plantilla(request):
    return render(request, 'plantilla.html', {'nombre': 'Juan'})


