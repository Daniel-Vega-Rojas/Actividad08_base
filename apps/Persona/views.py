from django.shortcuts import redirect, render
from django.http import HttpResponse
from apps.Persona.models import Persona
from apps.Persona.form import PersonaForm

# Create your views here.

def home(request):
    
    return render(request, 'base/base.html')


def index(request):
    persona = Persona.objects.all().order_by('-id')
    context = {'personas': persona}
    return render(request, 'persona/index.html', context)
    # return render(request,'persona/index.html')


# /////////////////////////////////////Codigo de Crear - mostrar///////////////////////////

def personaCreate(request):
    if (request.method == 'POST'):
        form = PersonaForm(request.POST)
        if  form.is_valid():
            form.save()

        
        return redirect('personas:index')

    else:
        form = PersonaForm()
        return render(request, 'persona/formPersona.html', {'form': form})


#  /////////////////////////////////////Codigo de actualizar///////////////////////////

def personaEdit(request,id_persona):

    persona = Persona.objects.get(pk=id_persona)

    if request.method == 'GET':
        form = PersonaForm(instance=persona)
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('personas:index')
    
    return render(request, 'persona/formPersona.html', {'form': form})

#  /////////////////////////////////////Codigo de Eliminar///////////////////////////

def personaEliminar(request,id_persona):

    persona = Persona.objects.get(pk=id_persona)

    if request.method == 'POST':
        persona.delete()
        return redirect('personas:index')

    return render(request, 'persona/personaEliminar.html', {'persona': persona})
    






  