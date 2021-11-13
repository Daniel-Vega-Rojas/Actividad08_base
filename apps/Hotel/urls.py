from django.urls import path, include

from apps.Hotel.views import index

app_name = "hoteles"
urlpatterns = [
    path('mostrar', index)
]
