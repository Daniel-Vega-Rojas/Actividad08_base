from django.urls import path, include

from apps.Hotel.views import index, hotelCreate, hotelEdit, hotelEliminar


app_name = "Hoteles"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', hotelCreate, name='hotelCreate'), 
    path('actualizar/<int:id_hotel>/', hotelEdit, name='hotelEdit'), 
    path('eliminar/<int:id_hotel>/', hotelEliminar, name='hotelEliminar'), 
]

