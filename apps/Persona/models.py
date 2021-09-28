from django.db import models

# Create your models here.


class Persona(models.Model):

    
    Nombre    = models.CharField(max_length=100)
    Apellido   = models.CharField(max_length=50)
    Direccion    = models.CharField(max_length=45)
    Telefono    = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombre


