from django import forms
from .models import *


class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['nombre', 'artista', 'year']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "year"]


class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ["talle", "disenio", "color"]
