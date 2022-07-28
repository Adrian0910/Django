from django.http import HttpResponse
from datetime import datetime
def saludo(request):
    return HttpResponse("Hola mundo")

def pan(request):
    return HttpResponse("Pan de muerto")

def dia(request):
    hoy = datetime.today()
    return HttpResponse(f'El dia de hoy es {hoy.strftime("%A, %d de %B de %Y")}')


