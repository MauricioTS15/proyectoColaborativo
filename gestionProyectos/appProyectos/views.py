from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from .models import Cliente, Empleado, Tarea, Proyecto
from .forms import ProyectoForm, TareaForm, ClienteForm, EmpleadoForm, LoginForm, SigninForm, UserForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from .filters import ProyectoFilter, TareaFilter, ClienteFilter, EmpleadoFilter

# devuelve un formulario para cambiar la contraseña
def UserUpdateView(request):
    if request.method == 'POST':
        form = UserForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('La contraseña se ha reestablecido correctamente'))
            return redirect('user')
    else:
        form = UserForm(request.user)
    return render(request, 'user.html', {
        'form': form
    })

# devuelve los nombres de los usuarios en formato JSON 
class GetUsers(View):
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        lista_usuarios = []
        for usuario in users:
            lista_usuarios.append(usuario.username)
        return JsonResponse(list(lista_usuarios), safe=False)

# devuelve un formulario de inicio de sesión
class LogInView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('index') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Usuario o contraseña incorrectas.')
        return self.render_to_response(self.get_context_data(form=form))

# devuelve un formulario para registrar un usuario
class SignInView(CreateView):
    template_name = 'signin.html'
    form_class = SigninForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse_lazy('index')

# devuelve la página principal
class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto'] = Proyecto.objects.last()
        context['tarea'] = Tarea.objects.last()
        context['cliente'] = Cliente.objects.last()
        context['empleado'] = Empleado.objects.last()
        return context

# devuelve el listado de proyectos
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    queryset = Proyecto.objects.order_by('id')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filterset.form
        return context
    
# devuelve los datos de un proyecto
class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['tarea_list'] = context['proyecto'].tarea_set.order_by('nombre')
        context['filter_form'] = self.filterset.form
        return context

# devuelve un formulario para crear un proyecto
class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_create_form'
        
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['filter_form'] = ProyectoFilter().form
        return context
    
    def get_success_url(self):
        return reverse_lazy('proyecto', kwargs={'pk': self.object.id})

# devuelve un formulario para modificar el proyecto
class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name_suffix = '_update_form'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context
    
    def get_success_url(self):
        return reverse_lazy('proyecto', kwargs={'pk': self.object.id})

# borra el proyecto
class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    context_object_name = 'proyecto'
    success_url = reverse_lazy('index proyectos')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_list'] = Proyecto.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve el listado de tareas
class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    queryset = Tarea.objects.order_by('id')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TareaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filterset.form
        return context

# devuelve los datos de una tarea
class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TareaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve un formulario para crear una tarea
class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name_suffix = '_create_form'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TareaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        context['filter_form'] = TareaFilter().form
        return context
    
    def get_success_url(self):
        return reverse_lazy('tarea', kwargs={'pk': self.object.id})

# devuelve un formulario para modificar la tarea
class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name_suffix = "_update_form"
    form_class = TareaForm

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TareaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context
    
    def get_success_url(self):
        return reverse_lazy('tarea', kwargs={'pk': self.object.id})

# borra la tarea
class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = "tarea"
    success_url = reverse_lazy('index tareas')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TareaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea_list'] = Tarea.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve el listado de clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    queryset = Cliente.objects.order_by('id')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClienteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filterset.form
        return context

# devuelve los datos de un cliente
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClienteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve un formulario para crear un cliente
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = '_create_form'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClienteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        context['filter_form'] = ClienteFilter().form
        return context
    
    def get_success_url(self):
        return reverse_lazy('cliente', kwargs={'pk': self.object.id})

# devuelve un formulario para modificar un cliente
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name_suffix = "_update_form"
    form_class = ClienteForm

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClienteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context
    
    def get_success_url(self):
        return reverse_lazy('cliente', kwargs={'pk': self.object.id})

# borra el cliente
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    context_object_name = "cliente"
    success_url = reverse_lazy('index clientes')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClienteFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_list'] = Cliente.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve el listado de empleados
class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('id')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmpleadoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filterset.form
        return context

# devuelve los datos de un empleado
class EmpleadoDetailView(LoginRequiredMixin, DetailView):
    model = Empleado

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmpleadoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context

# devuelve un formulario para crear un empleado
class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name_suffix = '_create_form'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmpleadoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        context['filter_form'] = EmpleadoFilter().form
        return context
    
    def get_success_url(self):
        return reverse_lazy('empleado', kwargs={'pk': self.object.id})

# devuelve un formulario para modificar un empleado
class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Empleado
    template_name_suffix = "_update_form"
    form_class = EmpleadoForm
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmpleadoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context
    
    def get_success_url(self):
        return reverse_lazy('empleado', kwargs={'pk': self.object.id})

# borra el empleado
class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    context_object_name = "empleado"
    success_url = reverse_lazy('index empleados')

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = EmpleadoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_list'] = Empleado.objects.order_by('id')
        context['filter_form'] = self.filterset.form
        return context
