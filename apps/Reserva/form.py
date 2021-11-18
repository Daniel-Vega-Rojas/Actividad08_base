from django import forms
from django.forms import fields, widgets
from apps.Reserva.models import Reserva



class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva

        fields = [
            'Fecha_ingreso',
            'Fecha_salida',
            'Hora_ingreso',
            'Hotel',
            'Persona',
            'Agencia_de_viaje'
            
        ]

        Labels = {
            'Fecha_ingreso': 'Ingrese fecha de ingreso',
            'Fecha_salida': 'Ingrese fecha de salida',
            'Hora_ingreso' :'ingrese hora ingreso',
            'Hotel' :'Ingrese la hora',
            'Persona' :'ingrese la persona',
            'Agencia_de_viaje' :'Ingrese la agencia de viaje '

        }

        widgets = {
            'Fecha_ingreso':forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_salida' :forms.TextInput(attrs={'class': 'form-control'}),
            'Hora_ingreso' :forms.TextInput(attrs={'class': 'form-control'}),
            'Hotel' :forms.Select(attrs={'class': 'form-control'}),
            'Persona' :forms.Select(attrs={'class': 'form-control'}),
            'Agencia_de_viaje' :forms.Select(attrs={'class': 'form-control'})

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }