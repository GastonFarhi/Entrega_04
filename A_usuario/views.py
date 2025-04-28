from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FormularioRegistro, FormularioEdicionPerfil
from .models import InfoUsuario
from django.views.generic.detail import DetailView


# Create your views here.
def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            InfoUsuario.objects.get_or_create(user=usuario)
            return redirect("main:index")
    else:
        formulario = AuthenticationForm()
    return render(request, "A_usuario/login.html", {"formulario": formulario})


def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("user:login")
    else:
        formulario = FormularioRegistro()
    return render(request, "A_usuario/registro.html", {"formulario": formulario})


@login_required
def editar_perfil(request):
    info_extra = request.user.info_extra
    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get("img_perfil"):
                info_extra.avatar = formulario.cleaned_data.get("img_perfil")
            info_extra.save()
            formulario.save()
            return redirect("main:index")
    else:
        formulario = FormularioEdicionPerfil()
    return render(request, "A_usuario/editar_perfil.html", {"formulario": formulario})


class VistaDatosPerfil(LoginRequiredMixin, DetailView):
    model = InfoUsuario
    template_name = "A_usuario/ver_perfil.html"
    context_object_name = "usuario"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fecha_nacimiento"] = self.object.fecha_nacimiento
        context[
            "img_perfil"] = self.request.user.infousuario.img_perfil.url \
            if self.request.user.infousuario.img_perfil else "/media/profile_01.jpg"
        return context

    def get_object(self, queryset=None):
        return InfoUsuario.objects.get(user=self.request.user)
