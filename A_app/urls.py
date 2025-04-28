from django.urls import path
from .views import *

app_name = "contenido"

urlpatterns = [
    path('discos/', vista_disco, name="disco"),
    path('libros/', vista_libro, name="libro"),
    path('remeras/', vista_remera, name="remera"),

    path('discos/<int:pk>/', VistaDetalleDisco.as_view(), name="detalle_disco"),
    path('libros/<int:pk>/', VistaDetalleLibro.as_view(), name="detalle_libro"),
    path('remeras/<int:pk>/', VistaDetalleRemera.as_view(), name="detalle_remera"),

    path('discos/<int:pk>/modificar/', VistaModificarDisco.as_view(), name="modificar_disco"),
    path('libros/<int:pk>/modificar/', VistaModificarLibro.as_view(), name="modificar_libro"),
    path('remeras/<int:pk>/modificar/', VistaModificarRemera.as_view(), name="modificar_remera"),

    path('discos/<int:pk>/eliminar/', VistaEliminarDisco.as_view(), name="eliminar_disco"),
    path('libros/<int:pk>/eliminar/', VistaEliminarLibro.as_view(), name="eliminar_libro"),
    path('remeras/<int:pk>/eliminar/', VistaEliminarRemera.as_view(), name="eliminar_remera"),

    path('discos/nuevo/', NuevoDisco.as_view(), name="nuevo_disco"),
    path('libros/nuevo/', LibroNuevo.as_view(), name="libro_nuevo"),
    path('remeras/nueva/', RemeraNueva.as_view(), name="remera_nueva"),
    path('discos/resultados/', BusquedaDisco.as_view(), name="resultado")
]
