from django.db import models


# Create your models here.
class Disco(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Título")
    artista = models.CharField(max_length=100, verbose_name="Artista")
    year = models.IntegerField(verbose_name="Año")

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    year = models.IntegerField(verbose_name="Año")

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Remera(models.Model):
    talle = models.CharField(max_length=6, verbose_name="Talle")
    disenio = models.CharField(max_length=100, verbose_name="Diseño")
    color = models.CharField(max_length=50, default="", verbose_name="Color")

    def __str__(self):
        return f"{self.disenio} - {self.talle}"
