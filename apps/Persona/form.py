from django import forms
from django.forms import fields, widgets
from apps.Persona.models import Persona


class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona

        fields = [
            'Nombre',
            'Apellido',
            'Direccion',
            'Telefono'
        ]

        Labels = {
            'Nombre': 'Ingrese Su Nombre',
            'Apellido': 'Ingrese su Apellido',
            'Direccion': 'Ingrese su Direccion',
            'Telefono' :'Digita tu Telefono'

        }

        widgets = {
            'Nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido':forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion' :forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono' :forms.TextInput(attrs={'class': 'form-control'}),

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }