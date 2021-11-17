from django.urls import path, include

from apps.Categoria.views import index, categoriaCreate, categoriaEdit, categoriaEliminar

app_name = "Categorias"
urlpatterns = [
    path('', index, name ='index'), 
    path('nuevo/', categoriaCreate, name='categoriaCreate'), 
    path('actualizar/<int:id_categoria>/', categoriaEdit, name='categoriaEdit'), 
    path('eliminar/<int:id_categoria>/', categoriaEliminar, name='categoriaEliminar'), 
]