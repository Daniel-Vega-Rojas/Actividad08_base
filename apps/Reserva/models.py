from django.db import models
from apps.Hotel.models import Hotel
from apps.Persona.models import Persona
from apps.Agencia_de_viaje.models import Agencia_de_viaje

# Create your models here.



class Reserva(models.Model):

    
    
    Fecha_ingreso    = models.DateField()
    Fecha_salida    = models.DateField()
    Hora_ingreso    = models.CharField(max_length=30)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Agencia_de_viaje = models.ForeignKey(Agencia_de_viaje, on_delete=models.CASCADE)

    def __str__(self):
        return self.Hora_ingreso

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"    



