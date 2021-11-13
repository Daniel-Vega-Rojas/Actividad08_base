from django.shortcuts import render

from apps.Persona.models import Persona

# Create your views here.

def index(request):
    persona = Persona.objects.all().order_by('-id')
    context = {'personas': persona}
    return render(request, 'persona/index.html', context)
    # return render(request,'persona/index.html')

    