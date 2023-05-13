
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import ProyectoForm, TareaForm, ClienteForm, EmpleadoForm, LoginForm, SigninForm, UserForm
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

# devuelve un formulario para cambiar la contraseña
def user(request):
    if request.method == 'POST':
        form = UserForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('La contraseña se ha reestablecido correctamente'))
            return redirect('user')
        else:
            messages.error(request, _('Corrije el error mostrado a continuación'))
    else:
        form = UserForm(request.user)
    return render(request, 'user.html', {
        'form': form
    })

# devuelve un formulario de inicio de sesión
class login(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('index', kwargs={'selector': 0}) 
    
    def form_invalid(self, form):
        messages.error(self.request,'Usuario o contraseña incorrectas.')
        return self.render_to_response(self.get_context_data(form=form))

# devuelve un formulario para registrar un usuario
class signin(CreateView):
    template_name = 'signin.html'
    form_class = SigninForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse_lazy('index', kwargs={'selector': 0})

# devuelve la página principal
class index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, selector=0, **kwargs):
        context = super().get_context_data(**kwargs)
        if (selector == 0):
            context['proyecto'] = Proyecto.objects.last()
            context['tarea'] = Tarea.objects.last()
            context['cliente'] = Cliente.objects.last()
            context['empleado'] = Empleado.objects.last()
            context['filtro'] = 'más nuev'
        elif (selector == 1):
            context['proyecto'] = Proyecto.objects.first()
            context['tarea'] = Tarea.objects.first()
            context['cliente'] = Cliente.objects.first()
            context['empleado'] = Empleado.objects.first()
            context['filtro'] = 'más antigu'
        elif (selector == 2):
            context['proyecto'] = Proyecto.objects.order_by(Lower('nombre')).first()
            context['tarea'] = Tarea.objects.order_by(Lower('nombre')).first()
            context['cliente'] = Cliente.objects.order_by(Lower('nombre')).first()
            context['empleado'] = Empleado.objects.order_by(Lower('nombre')).first()
            context['filtro'] = 'alfabéticamente primer'
        elif (selector == 3):
            context['proyecto'] = Proyecto.objects.order_by(Lower('nombre')).last()
            context['tarea'] = Tarea.objects.order_by(Lower('nombre')).last()
            context['cliente'] = Cliente.objects.order_by(Lower('nombre')).last()
            context['empleado'] = Empleado.objects.order_by(Lower('nombre')).last()
            context['filtro'] = 'alfabéticamente últim'
        return context

# devuelve el listado de proyectos
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('id')

# devuelve los datos de un proyecto
class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['tarea_list'] = context['proyecto'].tarea_set.order_by('nombre')
        return context

# devuelve un formulario para crear un proyecto
class ProyectoCreateView(LoginRequiredMixin, CreateView):
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
class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
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
class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    context_object_name = "proyecto"
    success_url = reverse_lazy('index proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        return context

# devuelve el listado de tareas
class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('id')

# devuelve los datos de una tarea
class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context

# devuelve un formulario para crear una tarea
class TareaCreateView(LoginRequiredMixin, CreateView):
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
class TareaUpdateView(LoginRequiredMixin, UpdateView):
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
class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = "tarea"
    success_url = reverse_lazy('index tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        return context

# devuelve el listado de clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('id')

# devuelve los datos de un cliente
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context

# devuelve un formulario para crear un cliente
class ClienteCreateView(LoginRequiredMixin, CreateView):
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
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
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
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    context_object_name = "cliente"
    success_url = reverse_lazy('index clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        return context

# devuelve el listado de empleados
class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('id')

# devuelve los datos de un empleado
class EmpleadoDetailView(LoginRequiredMixin, DetailView):
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context

# devuelve un formulario para crear un empleado
class EmpleadoCreateView(LoginRequiredMixin, CreateView):
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
class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
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
class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    context_object_name = "empleado"
    success_url = reverse_lazy('index empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        return context
