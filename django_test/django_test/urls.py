
from django.contrib import admin
from django.urls import path

from django_test.views import saludo #importamos la funcion de views.py 
from django_test.views import pan
from django_test.views import dia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='view_de_saludo'),
    path('pan/', pan, name='view_del_pan'),
    path('dia/', dia, name='view_del_dia'),
]

