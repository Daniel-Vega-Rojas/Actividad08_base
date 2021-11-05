from django.urls import path, include

from apps.Persona.views import index

app_name = "Personas"
urlpatterns = [
    path('mostrar', index)
]
