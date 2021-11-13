from django.shortcuts import render


from apps.Categoria.models import Categoria

# Create your views here.

def index(request):
    categoria = Categoria.objects.all().order_by('-id')
    context = {'categorias': categoria}
    return render(request, 'Categoria/index.html', context)




    # return render(request,'Categoria/index.html')

    