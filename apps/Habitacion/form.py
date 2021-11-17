from django import forms
from django.forms import fields, widgets
from apps.Habitacion.models import Habitacion


class HabitacionForm(forms.ModelForm):
    
    class Meta:
        model = Habitacion

        fields = [
            'Tipo_De_Habitaciones',
            'Hotel'
        ]

        Labels = {
            'Tipo_De_Habitaciones': 'Ingrese Nombre del tipo de habitacion',
            'Hotel': "hotel"
        }

        widgets = {
            'Tipo_De_Habitaciones':forms.TextInput(attrs={'class': 'form-control'}),
            'Hotel' :forms.Select(attrs={'class': 'form-control'})

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }