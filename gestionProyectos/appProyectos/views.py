from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Cliente, Empleado, Tarea, Proyecto

#devuelve la página principal
def index(request):
     return render(request, 'index.html')

#devuelve el listado de proyectos
def index_proyectos(request):
    proyectos = get_list_or_404(Proyecto.objects.order_by('nombre'))
    context = {'proyectos': proyectos}
    return render(request, 'index_proyectos.html', context)

#devuelve los detalles de un proyecto
def show_proyecto(request, proyecto_id):
	proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
	tareas =  proyecto.tarea_realizar.all()
	context = { 'proyecto': proyecto, 'tareas' : tareas }
	return render(request, 'proyecto.html', context)

# Devuelve los detalles de una tarea
def show_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    proyectos =  tarea.proyecto_set.all()
    context = { 'proyectos': proyectos, 'tarea' : tarea }
    return render(request, 'tarea.html', context)