from django.urls import path, include

from apps.Agencia_de_viaje.views import index, agencia_de_viajeCreate, agencia_de_viajeEdit, agencia_de_viajeEliminar


app_name = "Agencia_de_viajes"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', agencia_de_viajeCreate, name='agencia_de_viajeCreate'), 
    path('actualizar/<int:id_agencia_de_viaje>/', agencia_de_viajeEdit, name='agencia_de_viajeEdit'), 
    path('eliminar/<int:id_agencia_de_viaje>/', agencia_de_viajeEliminar, name='agencia_de_viajeEliminar'), 
]

