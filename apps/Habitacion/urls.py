from django.urls import path, include

from apps.Habitacion.views import index

app_name = "habitaciones"
urlpatterns = [
    path('mostrar', index)
]
