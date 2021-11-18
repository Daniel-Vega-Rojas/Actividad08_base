from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Reserva.models import Reserva
from apps.Reserva.form import ReservaForm




# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')

def index(request):
    reserva = Reserva.objects.all().order_by('-id')
    context = {'reserva': reserva}
    return render(request, 'Reserva/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')


    # /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def reservaCreate(request):
    if (request.method == 'POST'):
        form = ReservaForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('Reservas:index')

    else:
        form = ReservaForm()
        return render(request, 'Reserva/formReserva.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def reservaEdit(request,id_reserva):

    reserva = Reserva.objects.get(pk=id_reserva)

    if request.method == 'GET':
        form = ReservaForm(instance=reserva)
    else:
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
        return redirect('Reserva:index')
    
    return render(request, 'Reserva/formReserva.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def reservaEliminar(request,id_reserva):

    reserva = Reserva.objects.get(pk=id_reserva)

    if request.method == 'POST':
        reserva.delete()
        return redirect('reservas:index')

    return render(request, 'Reserva/reservaEliminar.html', {'Reserva': reserva})
    

    