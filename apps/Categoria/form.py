from django import forms
from django.forms import fields, widgets
from apps.Categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria 

        fields = [
            'Iva',
            'Descripcion'
        ]

        Labels = {
            'Iva': 'Ingrese El Iva',
            'Descripcion': 'Ingrese su Descripcion'
        }

        widgets = {
            'Iva':forms.TextInput(attrs={'class': 'form-control'}),
            'Descripcion':forms.TextInput(attrs={'class': 'form-control'}),

            # en el caso de que haya relaciones, se desglose un espacio para seleccionar
            # 'tipoClient' :forms.Select(attrs={'class': 'form-control'}),
        }