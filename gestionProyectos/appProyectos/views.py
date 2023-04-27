from django.shortcuts import render
from django.urls import reverse_lazy
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
class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context
    
    def get_success_url(self):
        return reverse_lazy('tarea', kwargs={'pk': self.object.id})

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
    
    def get_success_url(self):
        return reverse_lazy('tarea', kwargs={'pk': self.object.id})

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
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context
    
    def get_success_url(self):
        return reverse_lazy('cliente', kwargs={'pk': self.object.id})

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
    
    def get_success_url(self):
        return reverse_lazy('cliente', kwargs={'pk': self.object.id})

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
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name_suffix = '_create_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context
    
    def get_success_url(self):
        return reverse_lazy('empleado', kwargs={'pk': self.object.id})

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
    
    def get_success_url(self):
        return reverse_lazy('empleado', kwargs={'pk': self.object.id})

# borra el empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    context_object_name = "empleado"
    success_url = reverse_lazy('index empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context
