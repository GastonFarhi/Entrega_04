from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class InfoUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    img_perfil = models.ImageField(upload_to="img_perfil", null=True, blank=True)
