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

    path('discos/menu/', menu_disco, name="menu_disco"),
    path('libros/menu/', menu_libro, name="menu_libro"),
    path('remeras/menu/', menu_remera, name="menu_remera"),

    path('discos/nuevo/', NuevoDisco.as_view(), name="nuevo_disco"),
    path('libros/nuevo/', LibroNuevo.as_view(), name="libro_nuevo"),
    path('remeras/nueva/', RemeraNueva.as_view(), name="remera_nueva"),

    path('discos/busqueda/artista/', BusquedaDiscoArtista.as_view(), name="disco_r_artista"),
    path('discos/busqueda/titulo/', BusquedaDiscoTitulo.as_view(), name="disco_r_titulo"),
    path('discos/busqueda/año/', BusquedaDiscoAnio.as_view(), name="disco_r_anio"),

    path('libros/busqueda/titulo/', BusquedaLibroTitulo.as_view(), name="libro_r_titulo"),
    path('libros/busqueda/autor/', BusquedaLibroAutor.as_view(), name="libro_r_autor"),
    path('libros/busqueda/año/', BusquedaLibroAnio.as_view(), name="libro_r_anio"),

    path('remeras/busqueda/talle/', BusquedaRemeraTalle.as_view(), name="remera_r_talle"),
    path('remeras/busqueda/disenio/', BusquedaRemeraDisenio.as_view(), name="remera_r_disenio"),
    path('remeras/busqueda/color/', BusquedaRemeraColor.as_view(), name="remera_r_color"),
]
