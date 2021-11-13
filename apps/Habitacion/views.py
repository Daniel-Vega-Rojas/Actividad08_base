from django.shortcuts import render
from django.http import HttpResponse

from apps.Habitacion.models import Habitacion


# Create your views here.

def index(request):
    # return render(request,'Habitacion/index.html')
    # return HttpResponse ("hola mudno")
    habitacion = Habitacion.objects.all().order_by('-id')
    context = {'habitacion': habitacion}
    return render(request, 'Habitacion/index.html', context)
    

    