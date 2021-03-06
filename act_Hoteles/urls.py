"""act_Hoteles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.Persona.views import home
# from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', home),
    path('habitaciones/', include('apps.Habitacion.urls', namespace="habitaciones")),
    path('agencia_de_viajes/', include('apps.Agencia_de_viaje.urls', namespace="agencia_de_viajes")),
    path('personas/', include('apps.Persona.urls', namespace="personas")),
    path('categorias/', include('apps.Categoria.urls', namespace="categorias")),
    path('reservas/', include('apps.Reserva.urls', namespace="reservas")),
    path('hoteles/', include('apps.Hotel.urls', namespace="hoteles"))
]


