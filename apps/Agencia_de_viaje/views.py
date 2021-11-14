from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Agencia_de_viaje.models import Agencia_de_viaje
from apps.Agencia_de_viaje.form import Agencia_de_viajeForm




# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')

def index(request):
    agencia_de_viaje = Agencia_de_viaje.objects.all().order_by('-id')
    context = {'agencia_de_viajes': agencia_de_viaje}
    return render(request, 'Agencia_de_viaje/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')


    # /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def agencia_de_viajeCreate(request):
    if (request.method == 'POST'):
        form = Agencia_de_viajeForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('Agencia_de_viajes:index')

    else:
        form = Agencia_de_viajeForm()
        return render(request, 'Agencia_de_viaje/formAgencia_de_viaje.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def agencia_de_viajeEdit(request,id_agencia_de_viaje):

    agencia_de_viaje = Agencia_de_viaje.objects.get(pk=id_agencia_de_viaje)

    if request.method == 'GET':
        form = Agencia_de_viajeForm(instance=agencia_de_viaje)
    else:
        form = Agencia_de_viajeForm(request.POST, instance=agencia_de_viaje)
        if form.is_valid():
            form.save()
        return redirect('Agencia_de_viajes:index')
    
    return render(request, 'Agencia_de_viaje/formAgencia_de_viaje.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def agencia_de_viajeEliminar(request,id_agencia_de_viaje):

    agencia_de_viaje = Agencia_de_viaje.objects.get(pk=id_agencia_de_viaje)

    if request.method == 'POST':
        agencia_de_viaje.delete()
        return redirect('agencia_de_viajes:index')

    return render(request, 'Agencia_de_viaje/agencia_de_viajeEliminar.html', {'Agencia_de_viaje': agencia_de_viaje})
    

    