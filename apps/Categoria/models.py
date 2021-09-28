from django.db import models

class Categoria(models.Model):

    Iva = models.CharField(max_length=20)
    Descripcion   = models.CharField(max_length=80)


    def __str__(self):
        return self.Descripcion

