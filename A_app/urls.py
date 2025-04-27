from django.urls import path
from .views import *

app_name = "contenido"

urlpatterns = [
    path('discos/', vista_disco, name="disco"),
    path('libros/', vista_libro, name="libro"),
    path('remeras/', vista_remera, name="remera"),
    path('discos/nuevo/', NuevoDisco.as_view(), name="nuevo_disco"),
    path('libros/nuevo/', LibroNuevo.as_view(), name="libro_nuevo"),
    path('remeras/nueva/', RemeraNueva.as_view(), name="remera_nueva")
]
