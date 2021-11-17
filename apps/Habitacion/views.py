from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Habitacion.models import Habitacion
from apps.Habitacion.form import HabitacionForm




# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')

def index(request):
    habitacion = Habitacion.objects.all().order_by('-id')
    context = {'habitaciones': habitacion}
    return render(request, 'Habitacion/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')


    # /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def habitacionCreate(request):
    if (request.method == 'POST'):
        form = HabitacionForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('Habitaciones:index')

    else:
        form = HabitacionForm()
        return render(request, 'Habitacion/formHabitacion.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def habitacionEdit(request,id_habitacion):

    habitacion = Habitacion.objects.get(pk=id_habitacion)

    if request.method == 'GET':
        form = HabitacionForm(instance=habitacion)
    else:
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
        return redirect('Habitaciones:index')
    
    return render(request, 'Habitacion/formHabitacion.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def habitacionEliminar(request,id_habitacion):

    habitacion = Habitacion.objects.get(pk=id_habitacion)

    if request.method == 'POST':
        habitacion.delete()
        return redirect('habitaciones:index')

    return render(request, 'Habitacion/habitacionEliminar.html', {'Habitacion': habitacion})
    

    