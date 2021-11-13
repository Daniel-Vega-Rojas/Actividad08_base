from django.shortcuts import render


from apps.Reserva.models import Reserva

# Create your views here.

def index(request):
    reserva = Reserva.objects.all().order_by('-id')
    context = {'reservas': reserva}
    return render(request, 'Reserva/index.html', context)
    #return render(request,'Reserva/index.html')

    