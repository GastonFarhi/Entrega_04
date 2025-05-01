from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


# Create your views here.
def vista_disco(request):
    lista_discos = Disco.objects.all()
    return render(request, "A_app/disco.html", {"lista_discos": lista_discos})


def vista_remera(request):
    lista_remeras = Remera.objects.all()
    return render(request, "A_app/remera.html", {"lista_remeras": lista_remeras})


def vista_libro(request):
    lista_libros = Libro.objects.all()
    return render(request, "A_app/libro.html", {"lista_libros": lista_libros})


class NuevoDisco(LoginRequiredMixin, CreateView):
    model = Disco
    form_class = DiscoForm
    template_name = "A_app/submit_disco.html"
    success_url = reverse_lazy("contenido:disco")
    login_url = "user:login"


class LibroNuevo(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "A_app/submit_libro.html"
    success_url = reverse_lazy("contenido:libro")
    login_url = "user:login"


class RemeraNueva(LoginRequiredMixin, CreateView):
    model = Remera
    form_class = RemeraForm
    template_name = "A_app/submit_remera.html"
    success_url = reverse_lazy("contenido:remera")
    login_url = "user:login"


class BusquedaDisco(ListView):
    model = Disco
    template_name = "A_app/resultado.html"
    context_object_name = "resultados"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Disco.objects.filter(artista__icontains=buscar)
        return Disco.objects.none()


class VistaDetalleDisco(DetailView):
    model = Disco
    template_name = "A_app/detalle_disco.html"


class VistaDetalleLibro(DetailView):
    model = Libro
    template_name = "A_app/detalle_libro.html"


class VistaDetalleRemera(DetailView):
    model = Remera
    template_name = "A_app/detalle_remera.html"


class VistaModificarDisco(LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "A_app/modificar_disco.html"
    fields = ['nombre', 'artista', 'year']
    labels = {
        "nombre": "Nombre:",
        "artista": "Artista:",
        "year": "Año:"
    }
    success_url = reverse_lazy("contenido:disco")
    login_url = "user:login"


class VistaEliminarDisco(LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "A_app/modificar_disco.html"
    success_url = reverse_lazy("contenido:disco")
    login_url = "user:login"


class VistaModificarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "A_app/modificar_libro.html"
    fields = ['titulo', 'autor', 'year']
    labels = {
        "titulo": "Título:",
        "autor": "Autor:",
        "year": "Año:"
    }
    success_url = reverse_lazy("contenido:libro")
    login_url = "user:login"


class VistaEliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "A_app/modificar_libro.html"
    success_url = reverse_lazy("contenido:libro")
    login_url = "user:login"


class VistaModificarRemera(LoginRequiredMixin, UpdateView):
    model = Remera
    template_name = "A_app/modificar_remera.html"
    fields = ['talle', 'disenio', "color"]
    labels = {
        "talle": "Talle:",
        "disenio": "Diseño:",
        "color": "Color:",
    }
    success_url = reverse_lazy("contenido:remera")
    login_url = "user:login"


class VistaEliminarRemera(LoginRequiredMixin, DeleteView):
    model = Remera
    template_name = "A_app/modificar_remera.html"
    success_url = reverse_lazy("contenido:remera")
    login_url = "user:login"
