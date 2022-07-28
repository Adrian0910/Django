
from django.contrib import admin
from django.urls import path

from django_test.views import saludo #importamos la funcion de views.py 
from django_test.views import pan
from django_test.views import dia
from django_test.views import saludo_nombre
from django_test.views import fecha_nacimiento
from django_test.views import plantilla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='view_de_saludo'),
    path('pan/', pan, name='view_del_pan'),
    path('dia/', dia, name='view_del_dia'),
    path('saludo-nombre/<str:nombre>', saludo_nombre, name='saludo_con_nombre'), #agregamos el parametro nombre directamente en la url
    path('edad/<int:anio>', fecha_nacimiento, name='fecha_nacimiento'), #Calcular la edad
    path('plantilla/', plantilla, name='plantilla'),
]

