from django.urls import path, include

from apps.Reserva.views import index, reservaCreate, reservaEdit, reservaEliminar


app_name = "Reservas"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', reservaCreate, name='reservaCreate'), 
    path('actualizar/<int:id_reserva>/', reservaEdit, name='reservaEdit'), 
    path('eliminar/<int:id_reserva>/', reservaEliminar, name='reservaEliminar') 
]

