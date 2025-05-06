from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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


""" ********************************************* """
""" ******************* MENUS ******************* """
""" ********************************************* """


def menu_disco(request):
    return render(request, "A_app/menu_disco.html")


def menu_libro(request):
    return render(request, "A_app/menu_libro.html")


def menu_remera(request):
    return render(request, "A_app/menu_remera.html")


""" ********************************************* """
""" ****************** AGREGAR ****************** """
""" ********************************************* """


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


""" ********************************************* """
""" ************* BUSCAR EN DISCO *************** """
""" ********************************************* """


class BusquedaDiscoArtista(ListView):
    model = Disco
    template_name = "A_app/disc_busc_artista.html"
    context_object_name = "resultados_disco_artista"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Disco.objects.filter(artista__icontains=buscar)
        return Disco.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre_artista"] = self.request.GET.get("q", "")
        return context


class BusquedaDiscoTitulo(ListView):
    model = Disco
    template_name = "A_app/disc_busc_titulo.html"
    context_object_name = "resultados_disco_titulo"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Disco.objects.filter(nombre__icontains=buscar)
        return Disco.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_disco"] = self.request.GET.get("q", "")
        return context


class BusquedaDiscoAnio(ListView):
    model = Disco
    template_name = "A_app/disc_busc_anio.html"
    context_object_name = "resultados_disco_anio"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Disco.objects.filter(year__icontains=buscar)
        return Disco.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["año_lanzamiento"] = self.request.GET.get("q", "")
        return context


""" ********************************************* """
""" ************* BUSCAR EN LIBRO *************** """
""" ********************************************* """


class BusquedaLibroTitulo(ListView):
    model = Libro
    template_name = "A_app/libro_busc_titulo.html"
    context_object_name = "resultados_libro_titulo"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Libro.objects.filter(titulo__icontains=buscar)
        return Libro.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_libro"] = self.request.GET.get("q", "")
        return context


class BusquedaLibroAutor(ListView):
    model = Libro
    template_name = "A_app/libro_busc_autor.html"
    context_object_name = "resultados_libro_autor"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Libro.objects.filter(autor__icontains=buscar)
        return Libro.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autor_libro"] = self.request.GET.get("q", "")
        return context


class BusquedaLibroAnio(ListView):
    model = Libro
    template_name = "A_app/libro_busc_anio.html"
    context_object_name = "resultados_libro_anio"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Libro.objects.filter(year__icontains=buscar)
        return Libro.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["año_publicacion"] = self.request.GET.get("q", "")
        return context


""" ********************************************* """
""" ************ BUSCAR EN REMERA *************** """
""" ********************************************* """


class BusquedaRemeraTalle(ListView):
    model = Remera
    template_name = "A_app/rem_busc_talle.html"
    context_object_name = "resultados_remera_talle"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Remera.objects.filter(talle__icontains=buscar)
        return Remera.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["remera_talle"] = self.request.GET.get("q", "")
        return context


class BusquedaRemeraDisenio(ListView):
    model = Remera
    template_name = "A_app/rem_busc_disenio.html"
    context_object_name = "resultados_remera_disenio"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Remera.objects.filter(disenio__icontains=buscar)
        return Remera.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["remera_disenio"] = self.request.GET.get("q", "")
        return context


class BusquedaRemeraColor(ListView):
    model = Remera
    template_name = "A_app/rem_busc_color.html"
    context_object_name = "resultados_remera_color"
    login_url = "user:login"

    def get_queryset(self):
        buscar = self.request.GET.get("q", "")
        if buscar:
            return Remera.objects.filter(color__icontains=buscar)
        return Remera.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["remera_color"] = self.request.GET.get("q", "")
        return context


""" ********************************************* """
""" **************** VER DETALLE **************** """
""" ********************************************* """


class VistaDetalleDisco(DetailView):
    model = Disco
    template_name = "A_app/detalle_disco.html"


class VistaDetalleLibro(DetailView):
    model = Libro
    template_name = "A_app/detalle_libro.html"


class VistaDetalleRemera(DetailView):
    model = Remera
    template_name = "A_app/detalle_remera.html"


""" ********************************************* """
""" ***************** MODIFICAR ***************** """
""" ********************************************* """


class VistaModificarDisco(LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "A_app/modificar_disco.html"
    fields = ['nombre', 'artista', 'year']
    success_url = reverse_lazy("contenido:disco")
    login_url = "user:login"


class VistaModificarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "A_app/modificar_libro.html"
    fields = ['titulo', 'autor', 'year']
    success_url = reverse_lazy("contenido:libro")
    login_url = "user:login"


class VistaModificarRemera(LoginRequiredMixin, UpdateView):
    model = Remera
    template_name = "A_app/modificar_remera.html"
    fields = ['talle', 'disenio', "color"]
    success_url = reverse_lazy("contenido:remera")
    login_url = "user:login"


""" ********************************************* """
""" ****************** ELIMINAR ***************** """
""" ********************************************* """


class VistaEliminarDisco(LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "A_app/modificar_disco.html"
    success_url = reverse_lazy("contenido:disco")
    login_url = "user:login"


class VistaEliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "A_app/modificar_libro.html"
    success_url = reverse_lazy("contenido:libro")
    login_url = "user:login"


class VistaEliminarRemera(LoginRequiredMixin, DeleteView):
    model = Remera
    template_name = "A_app/modificar_remera.html"
    success_url = reverse_lazy("contenido:remera")
    login_url = "user:login"
