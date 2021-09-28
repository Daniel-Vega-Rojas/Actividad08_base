from django.db import models

from apps.Hotel.models import Hotel

# Create your models here.



class Habitacion(models.Model):

    Tipo_De_Habitaciones = models.CharField(max_length=45)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)



    def __str__(self):
        return self.Tipo_De_Habitaciones
    

