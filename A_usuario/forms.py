from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioRegistro(UserCreationForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TimeInput(attrs={"autocomplete": "off"}))

    date_joined = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Fecha de Nacimiento")

    username = forms.CharField(label="Nombre de Usuario", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    email = forms.EmailField(widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "date_joined", "username", "email", "password1",
                  "password2"]
        help_text = {key: "" for key in fields}


class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False, widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    first_name = forms.CharField(label="Nombre", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TimeInput(attrs={"autocomplete": "off"}))
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={"class": "custom-file-input"}))

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar"]
