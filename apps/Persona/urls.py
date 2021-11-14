from django.urls import path, include

from apps.Persona.views import index, personaCreate, personaEdit, personaEliminar

app_name = "Personas"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', personaCreate, name='personaCreate'), 
    path('actualizar/<int:id_persona>/', personaEdit, name='personaEdit'), 
    path('eliminar/<int:id_persona>/', personaEliminar, name='personaEliminar'), 
]
