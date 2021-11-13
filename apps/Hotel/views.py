from django.shortcuts import render
from django.http import HttpResponse

from apps.Hotel.models import Hotel

# Create your views here.
def index(request):
    # return render(request,'Habitacion/index.html')
    # return HttpResponse ("hola mudno")
    hotel = Hotel.objects.all().order_by('-id')
    context = {'hotel': hotel}
    return render(request, 'Hotel/index.html', context)