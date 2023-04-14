from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Cliente, Empleado, Tarea, Proyecto

# devuelve la página principal
def index(request):
    return render(request, 'index.html')

# devuelve el listado de proyectos
def index_proyectos(request):
    proyectos = get_list_or_404(Proyecto.objects.order_by('nombre'))
    context = {'proyectos': proyectos}
    return render(request, 'index_proyectos.html', context)

# devuelve los datos de un proyecto
def show_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    tareas = proyecto.tarea_realizar.all()
    context = {'proyecto': proyecto, 'tareas': tareas}
    return render(request, 'proyecto.html', context)

# devuelve un formaulario para crear un proyecto
def ins_proyecto(request):
    clientes = get_list_or_404(Cliente.objects.order_by('nombre'))
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    tareas = get_list_or_404(Tarea.objects.order_by('nombre'))
    context = {'clientes': clientes, 'responsables': responsables, 'tareas': tareas}
    return render(request, 'ins_proyecto.html', context)

# devuelve un formulario para modificar el proyecto
def mod_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    clientes = get_list_or_404(Cliente.objects.order_by('nombre'))
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    tareas = get_list_or_404(Tarea.objects.order_by('nombre'))
    context = {'proyecto': proyecto, 'clientes': clientes, 'responsables': responsables, 'tareas': tareas}
    return render(request, 'mod_proyecto.html', context)

# devuelve los datos de una tarea
def show_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    proyectos = tarea.proyecto_set.all()
    context = {'proyectos': proyectos, 'tarea': tarea}
    return render(request, 'tarea.html', context)

# devuelve un formulario para crear una tarea
def ins_tarea(request):
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    context = {'responsables': responsables}
    return render(request, 'mod_tarea.html', context)

# devuelve un formulario para modificar la tarea
def mod_tarea(request, tarea_id):
    tarea = get_object_or_404(Proyecto, pk=tarea_id)
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    context = {'tarea': tarea, 'responsables': responsables}
    return render(request, 'mod_tarea.html', context)

# devuelve el listado de clientes
def index_clientes(request):
    clientes = get_list_or_404(Cliente.objects.order_by('nombre'))
    context = {'clientes': clientes}
    return render(request, 'index_clientes.html', context)

# devuelve los datos de un cliente
def show_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    context = {'cliente': cliente}
    return render(request, 'cliente.html', context)

# devuelve el listado de empleados
def index_empleados(request):
    empleados = get_list_or_404(Empleado.objects.order_by('nombre'))
    context = {'empleados': empleados}
    return render(request, 'index_empleados.html', context)

# devuelve los datos de un empleado
def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    context = {'empleado': empleado}
    return render(request, 'empleado.html', context)
