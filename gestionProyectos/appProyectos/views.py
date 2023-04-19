from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import RegProyectoForm, RegTareaForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = context['proyecto'].tarea_set.all()
        return context

# devuelve un formulario para crear un proyecto
class ProyectoCreateView(View):
    # mostrar el formulario vacío
    def get(self, request, *args, **kwargs):
        form = RegProyectoForm()
        return render(request, 'reg_proyecto.html', {'form': form})

    # registrar el proyecto
    def post(self, request, *args, **kwargs):
        form = RegProyectoForm(request.POST)
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
            return redirect('index proyectos')
        return render(request, 'reg_proyecto.html', {'form': form})

# devuelve un formulario para modificar el proyecto
class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name_suffix = "_update_form"
    form_class = RegProyectoForm
    success_url = reverse_lazy('index proyectos')
    

# borra el proyecto
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    context_object_name = "proyecto"
    success_url = reverse_lazy('index proyectos')

# devuelve el listado de tareas
class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('nombre')

# devuelve los datos de una tarea
class TareaDetailView(DetailView):
    model = Tarea

# devuelve un formulario para crear una tarea
class TareaCreateView(View):
    # mostrar el formulario vacío
    def get(self, request, *args, **kwargs):
        form = RegTareaForm()
        return render(request, 'reg_tarea.html', {'form': form})
    
    # registrar la tarea
    def post(self, request, *args, **kwargs):
        form = RegTareaForm(request.POST)
        if form.is_valid():
            tarea = Tarea()
            tarea.nombre = form.cleaned_data['nombre']
            tarea.descripcion = form.cleaned_data['descripcion']
            tarea.fecha_inicio = form.cleaned_data['fecha_inicio']
            tarea.fecha_fin = form.cleaned_data['fecha_fin']
            tarea.responsable = form.cleaned_data['responsable']
            tarea.estado = form.cleaned_data['estado']
            tarea.prioridad = form.cleaned_data['prioridad']
            tarea.notas = form.cleaned_data['notas']
            tarea.proyecto = form.cleaned_data['proyecto']
            tarea.save()
            return redirect('index tareas')
        return render(request, 'reg_tarea.html', {'form': form})

# devuelve un formulario para modificar la tarea
class TareaUpdateView(UpdateView):
    model = Tarea
    template_name_suffix = "_update_form"
    form_class = RegTareaForm
    success_url = reverse_lazy('index tareas')

# borra la tarea
class TareaDeleteView(DeleteView):
    model = Tarea
    context_object_name = "tarea"
    success_url = reverse_lazy('index tareas')

# devuelve el listado de clientes
class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('nombre')

# devuelve los datos de un cliente
class ClienteDetailView(DetailView):
    model = Cliente

# devuelve el listado de empleados
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')

# devuelve los datos de un empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
