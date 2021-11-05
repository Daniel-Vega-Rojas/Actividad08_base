from django.urls import path, include

from apps.Agencia_de_viaje.views import index

app_name = "Agencia_de_viajes"
urlpatterns = [
    path('mostrar', index)
]
