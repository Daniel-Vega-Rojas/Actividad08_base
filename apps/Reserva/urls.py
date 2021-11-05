from django.urls import path, include

from apps.Reserva.views import index

app_name = "Reservas"
urlpatterns = [
    path('mostrar', index)
]