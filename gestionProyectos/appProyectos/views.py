from django.http import HttpResponse
from django.shortcuts import render
from .models import Proyecto

def index(request):
    proyectos = Proyecto.objects.all()
    context = {'proyectos': proyectos}
    return render(request, 'index.html', context)
