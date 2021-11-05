from django.db import models
from apps.Categoria.models import Categoria

# Create your models here.

class Hotel(models.Model):

    Nombre = models.CharField(max_length=100)
    Direccion    = models.CharField(max_length=45)
    Año_contruccion     = models.CharField(max_length=10)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hoteles"    


    