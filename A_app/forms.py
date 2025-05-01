from django import forms
from .models import *


class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['nombre', 'artista', 'year']
        labels = {
            "nombre": "Nombre:",
            "artista": "Artista:",
            "year": "Año:"
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "year"]
        labels = {
            "titulo": "Título:",
            "autor": "Autor:",
            "year": "Año:",
        }


class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ["talle", "disenio", "color"]
        labels = {
            "talle": "Talle:",
            "disenio": "Diseño:",
            "color": "Color:",
        }
