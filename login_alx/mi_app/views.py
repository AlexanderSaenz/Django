from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto

def hola_mundo(request):
    return HttpResponse("¡Hola, Django!")

def inicio(request):
    return HttpResponse("Iniciooooooo")


def portafolio(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'mi_app/portafolio.html', {'proyectos': proyectos})



def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})