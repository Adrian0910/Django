
from django.contrib import admin
from django.urls import path

from django_test.views import saludo #importamos la funcion de views.py 
from django_test.views import pan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='view_de_saludo'),
    path('pan/', pan, name='view_del_pan'),
]
