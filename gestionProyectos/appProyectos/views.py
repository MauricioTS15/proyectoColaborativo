from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import RegProyectoForm, RegTareaForm, RegClienteForm,RegEmpleadoForm

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

class ClienteCreateView(View):
    def get(self, request, *args, **kwargs):
        form = RegClienteForm()
        return render(request, 'reg_cliente.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.dni = form.cleaned_data['dni']
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.email = form.cleaned_data['email']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.save()
            return redirect('index clientes')
        return render(request, 'reg_cliente.html', {'form': form})

# devuelve un formulario para modificar un cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name_suffix = "_update_form"
    form_class = RegClienteForm
    success_url = reverse_lazy('index clientes')

# borra el cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    context_object_name = "cliente"
    success_url = reverse_lazy('index clientes')

# devuelve el listado de empleados
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('nombre')

# devuelve los datos de un empleado
class EmpleadoDetailView(DetailView):
    model = Empleado

class EmpleadoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = RegEmpleadoForm()
        return render(request, 'reg_empleado.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegClienteForm(request.POST)
        if form.is_valid():
            empleado = Empleado()
            empleado.dni = form.cleaned_data['dni']
            empleado.nombre = form.cleaned_data['nombre']
            empleado.apellido = form.cleaned_data['apellido']
            empleado.email = form.cleaned_data['email']
            empleado.telefono = form.cleaned_data['telefono']
            empleado.save()
            return redirect('index empleados')
        return render(request, 'reg_empleado.html', {'form': form})

# devuelve un formulario para modificar un empleado
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name_suffix = "_update_form"
    form_class = RegEmpleadoForm
    success_url = reverse_lazy('index empleados')

# borra el empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    context_object_name = "empleado"
    success_url = reverse_lazy('index empleados')
