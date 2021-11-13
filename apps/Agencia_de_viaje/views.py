from django.shortcuts import render

from apps.Agencia_de_viaje.models import Agencia_de_viaje

# Create your views here.

def index(request):
    agencia_de_viaje = Agencia_de_viaje.objects.all().order_by('-id')
    context = {'agencia_de_viajes': agencia_de_viaje}
    return render(request, 'Agencia_de_viaje/index.html', context)
    # return render(request,'Agencia_de_viaje/index.html')

    