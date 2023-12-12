from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.models import Persona


# Create your views here.
def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona,pk=id)
    return render (request,'personas/detalle.html',{'persona':persona})

PersonaForm = modelform_factory(Persona,exclude=[])





def nuevaPersona (request):
    if request.method == 'POST': #crear objeto
        formaPersona = PersonaForm(request.POST) #Formulario lleno
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect ('inicio')
        else:#cuando hay formulario con errores
            return render(request,'personas/nuevo.Html',{'formaPersona':formaPersona})

    else:#solicitar el formulario vacio GET
        formaPersona = PersonaForm()
        return render(request, 'personas/nuevo.Html', {'formaPersona': formaPersona})

def BorrarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')

def editarPersona(request,id):
    if request.method == 'POST':
        persona = get_object_or_404(Persona, pk=id)
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
        else:#Se activa cuando is_valid es falso
            return render(request, 'personas/editar.Html', {'formaPersona': formaPersona})
    else:#Cuando es Get (pido formulario lleno con informacion de la BD hasta ese momento), aqui recien voy a editar primera fase
        persona = get_object_or_404(Persona, pk=id)
        formaPersona = PersonaForm(instance=persona) #Formulario lleno
        return render(request, 'personas/editar.Html', {'formaPersona': formaPersona})