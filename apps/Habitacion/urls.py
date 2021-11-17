from django.urls import path, include

from apps.Habitacion.views import index, habitacionCreate, habitacionEdit, habitacionEliminar


app_name = "Habitaciones"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', habitacionCreate, name='habitacionCreate'), 
    path('actualizar/<int:id_habitacion>/', habitacionEdit, name='habitacionEdit'), 
    path('eliminar/<int:id_habitacion>/', habitacionEliminar, name='habitacionEliminar'), 
]
