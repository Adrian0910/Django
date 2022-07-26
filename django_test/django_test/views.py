from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def pan(request):
    return HttpResponse("Pan de muerto")

