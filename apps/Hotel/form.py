from django import forms
from django.forms import fields, widgets
from apps.Hotel.models import Hotel


class HotelForm(forms.ModelForm):
    
    class Meta:
        model = Hotel

        fields = [
            'Nombre',
            'Direccion',
            'Año_contruccion',
            'Categoria'
        ]

        Labels = {
            'Nombre': 'Ingrese Nombre de Agencia',
            'Direccion': 'Ingrese su Direccion',
            'Año_contruccion' :'ingrese el año de construccion',
            'Categoria' :'Ingrese la categoria'

        }

        widgets = {
            'Nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion' :forms.TextInput(attrs={'class': 'form-control'}),
            'Año_contruccion' :forms.TextInput(attrs={'class': 'form-control'}),
            # 'Categoria' :forms.TextInput(attrs={'class': 'form-control'}),
            'Categoria' :forms.Select(attrs={'class': 'form-control'})

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }