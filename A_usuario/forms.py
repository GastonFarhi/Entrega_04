from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioRegistro(UserCreationForm):
    img_perfil = forms.ImageField(required=False)
    first_name = forms.CharField(label="Nombre", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento",
                                       widget=forms.DateInput(attrs={"type": "date", "autocomplete": "off"}))
    username = forms.CharField(label="Nombre de Usuario", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    email = forms.EmailField(widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["img_perfil", "first_name", "last_name", "fecha_nacimiento", "username", "email", "password1",
                  "password2"]
        help_text = {key: "" for key in fields}


class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False, widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    first_name = forms.CharField(label="Nombre", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    img_perfil = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "img_perfil"]
