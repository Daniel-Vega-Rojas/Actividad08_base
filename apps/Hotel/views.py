from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Hotel.models import Hotel
from apps.Hotel.form import HotelForm




# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')

def index(request):
    hotel = Hotel.objects.all().order_by('-id')
    context = {'hoteles': hotel}
    return render(request, 'Hotel/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')


    # /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def hotelCreate(request):
    if (request.method == 'POST'):
        form = HotelForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('Hoteles:index')

    else:
        form = HotelForm()
        return render(request, 'Hotel/formHotel.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def hotelEdit(request,id_hotel):

    hotel = Hotel.objects.get(pk=id_hotel)

    if request.method == 'GET':
        form = HotelForm(instance=hotel)
    else:
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
        return redirect('Hotel:index')
    
    return render(request, 'Hotel/formHotel.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def hotelEliminar(request,id_hotel):

    hotel = Hotel.objects.get(pk=id_hotel)

    if request.method == 'POST':
        hotel.delete()
        return redirect('hoteles:index')

    return render(request, 'Hotel/hotelEliminar.html', {'Hotel': hotel})
    

    