from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import ProyectoForm, TareaForm, ClienteForm, EmpleadoForm

# devuelve la página principal
def index(request):
    proyecto = Proyecto.objects.last()
    tarea = Tarea.objects.last()
    cliente = Cliente.objects.last()
    empleado = Empleado.objects.last()
    context = {'proyecto': proyecto, 'tarea': tarea, 'cliente': cliente, 'empleado': empleado}
    return render(request, 'index.html', context)

# devuelve el listado de proyectos
class ProyectoListView(ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('id')

# devuelve los datos de un proyecto
class ProyectoDetailView(DetailView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['tarea_list'] = context['proyecto'].tarea_set.order_by('nombre')
        return context

# devuelve un formulario para crear un proyecto
class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        return context
    
    def get_success_url(self):
        return reverse_lazy('proyecto', kwargs={'pk': self.object.id})

# devuelve un formulario para modificar el proyecto
class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        return context
    
    def get_success_url(self):
        return reverse_lazy('proyecto', kwargs={'pk': self.object.id})

# borra el proyecto
class ProyectoDeleteView(DeleteView):
    model = Proyecto
    context_object_name = "proyecto"
    success_url = reverse_lazy('index proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        return context

# devuelve el listado de tareas
class TareaListView(ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('id')

# devuelve los datos de una tarea
class TareaDetailView(DetailView):
    model = Tarea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context

# devuelve un formulario para crear una tarea
class TareaCreateView(View):
    # mostrar el formulario vacío
    def get(self, request, *args, **kwargs):
        tarea_list = Tarea.objects.order_by('id')
        form = TareaForm()
        context = {'tarea_list': tarea_list, 'form': form}
        return render(request, 'reg_tarea.html', context)
    
    # registrar la tarea
    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
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
    form_class = TareaForm
    success_url = reverse_lazy('index tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context

# borra la tarea
class TareaDeleteView(DeleteView):
    model = Tarea
    context_object_name = "tarea"
    success_url = reverse_lazy('index tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context

# devuelve el listado de clientes
class ClienteListView(ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('id')

# devuelve los datos de un cliente
class ClienteDetailView(DetailView):
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context

# devuelve un formulario para crear un cliente
class ClienteCreateView(View):
    def get(self, request, *args, **kwargs):
        cliente_list = Cliente.objects.order_by('id')
        form = ClienteForm()
        context = {'cliente_list': cliente_list, 'form': form}
        return render(request, 'reg_cliente.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
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
    form_class = ClienteForm
    success_url = reverse_lazy('index clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context

# borra el cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    context_object_name = "cliente"
    success_url = reverse_lazy('index clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context

# devuelve el listado de empleados
class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('id')

# devuelve los datos de un empleado
class EmpleadoDetailView(DetailView):
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context

# devuelve un formulario para crear un empleado
class EmpleadoCreateView(View):
    def get(self, request, *args, **kwargs):
        empleado_list = Empleado.objects.order_by('id')
        form = EmpleadoForm()
        context = {'empleado_list': empleado_list, 'form': form}
        return render(request, 'reg_empleado.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
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
    form_class = EmpleadoForm
    success_url = reverse_lazy('index empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context

# borra el empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    context_object_name = "empleado"
    success_url = reverse_lazy('index empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context
