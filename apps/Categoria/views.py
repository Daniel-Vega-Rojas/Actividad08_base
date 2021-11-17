from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Categoria.models import Categoria
from apps.Categoria.form import CategoriaForm




# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')

def index(request):
    categoria = Categoria.objects.all().order_by('-id')
    context = {'categorias': categoria}
    return render(request, 'Categoria/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')


    # /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def categoriaCreate(request):
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('Categorias:index')

    else:
        form = CategoriaForm()
        return render(request, 'Categoria/formCategoria.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def categoriaEdit(request,id_categoria):

    categoria = Categoria.objects.get(pk=id_categoria)

    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        return redirect('Categorias:index')
    
    return render(request, 'Categoria/formCategoria.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def categoriaEliminar(request,id_categoria):

    categoria = Categoria.objects.get(pk=id_categoria)

    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias:index')

    return render(request, 'Categoria/categoriaEliminar.html', {'Categoria': categoria})
    

    