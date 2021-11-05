from django.urls import path, include

from apps.Categoria.views import index

app_name = "Categorias"
urlpatterns = [
    path('mostrar', index)
]