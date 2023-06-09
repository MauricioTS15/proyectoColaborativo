from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('get_users/', views.GetUsers.as_view(), name='lista usuarios'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('user/', views.UserUpdateView, name='user'),
    # proyectos
    path('proyectos/', views.ProyectoListView.as_view(), name='index proyectos'),
    path('proyectos/reg_proyecto', views.ProyectoCreateView.as_view(), name='registrar proyecto'),
    path('proyectos/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('proyectos/<int:pk>/proyecto_update_form', views.ProyectoUpdateView.as_view(), name='modificar proyecto'),
    path('proyectos/<int:pk>/proyecto_confirm_delete', views.ProyectoDeleteView.as_view(), name='borrar proyecto'),
    # tareas
    path('tareas/', views.TareaListView.as_view(), name='index tareas'),
    path('tareas/reg_tarea', views.TareaCreateView.as_view(), name='registrar tarea'),
    path('tareas/<int:pk>', views.TareaDetailView.as_view(), name='tarea'),
    path('tareas/<int:pk>/tarea_update_form', views.TareaUpdateView.as_view(), name='modificar tarea'),
    path('tareas/<int:pk>/tarea_confirm_delete', views.TareaDeleteView.as_view(), name='borrar tarea'),
    # clientes
    path('clientes/', views.ClienteListView.as_view(), name='index clientes'),
    path('clientes/reg_cliente', views.ClienteCreateView.as_view(), name='registrar cliente'),
    path('clientes/<int:pk>', views.ClienteDetailView.as_view(), name='cliente'),
    path('clientes/<int:pk>/cliente_update_form', views.ClienteUpdateView.as_view(), name='modificar cliente'),
    path('clientes/<int:pk>/cliente_confirm_delete', views.ClienteDeleteView.as_view(), name='borrar cliente'),
    # empleados
    path('empleados/', views.EmpleadoListView.as_view(), name='index empleados'),
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('empleados/reg_empleado', views.EmpleadoCreateView.as_view(), name='registrar empleado'),
    path('empleados/<int:pk>/empleado_update_form', views.EmpleadoUpdateView.as_view(), name='modificar empleado'),
    path('empleados/<int:pk>/empleado_confirm_delete', views.EmpleadoDeleteView.as_view(), name='borrar empleado'),
]
