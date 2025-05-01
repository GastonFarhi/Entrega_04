from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "user"

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name="A_usuario/logout.html"), name="logout"),
    path('registro/', registro, name="registro"),
    path('perfil/editar/', editar_perfil, name="editar_perfil"),
    path('perfil/ver/', VistaDatosPerfil.as_view(), name="ver_perfil"),
]
