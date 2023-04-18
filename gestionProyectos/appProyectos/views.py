from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.shortcuts import render
from django.views import View
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import RegProyecto, TareaForm
from django.views.generic import DetailView, ListView

# devuelve la página principal


def index(request):
    return render(request, 'index.html')

# devuelve el listado de proyectos


class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('nombre')

# devuelve los datos de un proyecto


class ProyectoDetailView(DetailView):
    model = Proyecto

# def show_proyecto(request, proyecto_id):
#     proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
#     tareas = proyecto.tareas.all()
#     context = {'proyecto': proyecto, 'tareas': tareas}
#     return render(request, 'proyecto.html', context)


class ProyectoCreateView(View):

    # Llamada para mostrar la página con el formulario
    def get(self, request, *args, **kwargs):
        form = RegProyecto()
        return render(request, 'reg_proyecto.html', {'form': form})

    # Llamada para mostrar la creación del proyecto
    def post(self, request, *args, **kwargs):
        form = RegProyecto(request.POST)
        if form.is_valid():
            proyecto = Proyecto()
            proyecto.nombre = form.cleaned_data['nombre']
            proyecto.descripcion = form.cleaned_data['descripcion']
            proyecto.fecha_inicio = form.cleaned_data['fecha_inicio']
            proyecto.fecha_fin = form.cleaned_data['fecha_fin']
            proyecto.cliente = form.cleaned_data['cliente']
            proyecto.responsable = form.cleaned_data['responsable']
            proyecto.presupuesto = form.cleaned_data['presupuesto']
            proyecto.save()
            return redirect('proyecto_list.html')
        return render(request, 'reg_proyecto.html', {'form': form})


# devuelve un formulario para modificar el proyecto
def mod_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    clientes = get_list_or_404(Cliente.objects.order_by('nombre'))
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    tareas = get_list_or_404(Tarea.objects.order_by('nombre'))
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            responsable = form.cleaned_data['responsable']
            presupuesto = form.cleaned_data['presupuesto']
            cliente = form.cleaned_data['cliente']
            tareas = form.cleaned_data['tareas']
            Proyecto.objects.update(id=proyecto_id, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio,
                                    fecha_fin=fecha_fin, presupuesto=presupuesto, cliente=cliente, tareas=tareas, responsable=responsable)
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    context = {'form': form, 'proyecto': proyecto, 'clientes': clientes,
               'responsables': responsables, 'tareas': tareas}
    return render(request, 'mod_proyecto.html', context)

# devuelve el listado de tareas


class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')

# devuelve los datos de una tarea


class TareaDetailView(DetailView):
    model = Tarea

# def show_tarea(request, tarea_id):
#     tarea = get_object_or_404(Tarea, pk=tarea_id)
#     context = {'tarea': tarea}
#     return render(request, 'tarea.html', context)

# devuelve un formulario para crear una tarea


def reg_tarea(request):
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            responsable = form.cleaned_data['responsable']
            prioridad = form.cleaned_data['prioridad']
            estado = form.cleaned_data['estado']
            notas = form.cleaned_data['notas']
            Tarea.objects.update(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio,
                                 fecha_fin=fecha_fin, responsable=responsable, prioridad=prioridad, estado=estado, notas=notas)
            return redirect('proyectos')
    else:
        form = TareaForm()
    context = {'form': form, 'responsables': responsables}
    return render(request, 'reg_tarea.html', context)

# devuelve un formulario para modificar la tarea


def mod_tarea(request, tarea_id):
    tarea = get_object_or_404(Proyecto, pk=tarea_id)
    responsables = get_list_or_404(Empleado.objects.order_by('nombre'))
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            responsable = form.cleaned_data['responsable']
            prioridad = form.cleaned_data['prioridad']
            estado = form.cleaned_data['estado']
            notas = form.cleaned_data['notas']
            Tarea.objects.update(id=tarea_id, nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio,
                                 fecha_fin=fecha_fin, responsable=responsable, prioridad=prioridad, estado=estado, notas=notas)
            return redirect('proyectos')
    else:
        form = TareaForm()
    context = {'form': form, 'tarea': tarea, 'responsables': responsables}
    return render(request, 'mod_tarea.html', context)

# devuelve el listado de clientes


class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre')

# devuelve los datos de un cliente


class ClienteDetailView(DetailView):
    model = Cliente

# def show_cliente(request, cliente_id):
#     cliente = get_object_or_404(Cliente, pk=cliente_id)
#     context = {'cliente': cliente}
#     return render(request, 'cliente.html', context)

# devuelve el listado de empleados


class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')

# devuelve los datos de un empleado


class EmpleadoDetailView(DetailView):
    model = Empleado

# def show_empleado(request, empleado_id):
#     empleado = get_object_or_404(Empleado, pk=empleado_id)
#     context = {'empleado': empleado}
#     return render(request, 'empleado.html', context)

# DETAILVIEW
# class EmpleadoDetail(DetailView):
#     model = Empleado

#     def get_context_data(self, **kwargs):
#     # Cargar el contexto base
#         context = super().get_context_data(**kwargs)
#         # Añadir un listado de departamentos
#         context['departamento_list'] = Departamento.objects.all()
#         return context
