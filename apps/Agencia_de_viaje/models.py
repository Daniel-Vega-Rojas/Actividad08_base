from django.db import models

# Create your models here.


class Agencia_de_viaje(models.Model):

    
    Nombre    = models.CharField(max_length=100)
    Direccion    = models.CharField(max_length=45)
    Telefono    = models.CharField(max_length=15)
    Ciudad    = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombre



    class Meta:
        verbose_name = "Agencia_de_viaje"
        verbose_name_plural = "Agencia_de_viajes"



