from django.db import models


# Create your models here.
class Disco(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Remera(models.Model):
    talle = models.CharField(max_length=6)
    disenio = models.CharField(max_length=100)
    color = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.disenio} - {self.talle}"
