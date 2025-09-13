from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto, MenuItem

def hola_mundo(request):
    return HttpResponse("¡Hola, Django!")

def inicio(request):
    return HttpResponse("Iniciooooooo")


def portafolio(request):
    proyectos = Proyecto.objects.all()
    menu_items = MenuItem.objects.all().order_by('orden')
    return render(request, 'mi_app/portafolio.html', {'proyectos': proyectos, 'menu_items': menu_items})



def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

