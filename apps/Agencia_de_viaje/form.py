from django import forms
from django.forms import fields, widgets
from apps.Agencia_de_viaje.models import Agencia_de_viaje


class Agencia_de_viajeForm(forms.ModelForm):
    
    class Meta:
        model = Agencia_de_viaje

        fields = [
            'Nombre',
            'Direccion',
            'Telefono',
            'Ciudad'
        ]

        Labels = {
            'Nombre': 'Ingrese Nombre de Agencia',
            'Direccion': 'Ingrese su Direccion',
            'Telefono' :'Digita tu Telefono',
            'Ciudad' :'Ingrese su Ciudad'

        }

        widgets = {
            'Nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion' :forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono' :forms.TextInput(attrs={'class': 'form-control'}),
            'Ciudad' :forms.TextInput(attrs={'class': 'form-control'}),

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }