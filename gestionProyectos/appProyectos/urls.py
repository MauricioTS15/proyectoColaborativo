from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.ProyectoListView.as_view(), name='index proyectos'),
    path('proyectos/reg_proyecto', views.ProyectoCreateView.as_view(), name='registrar proyecto'),
    path('proyectos/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto'),
    path('proyectos/<int:pk>/proyecto_update_form', views.ProyectoUpdateView.as_view(), name='modificar proyecto'),
    path('proyectos/<int:pk>/proyecto_confirm_delete', views.ProyectoDeleteView.as_view(), name='borrar proyecto'),
    path('tareas/', views.TareaListView.as_view(), name='index tareas'),
    path('tareas/reg_tarea', views.TareaCreateView.as_view(), name='registrar tarea'),
    path('tareas/<int:pk>', views.TareaDetailView.as_view(), name='tarea'),
    path('tareas/<int:pk>/tarea_update_form', views.TareaUpdateView.as_view(), name='modificar tarea'),
    path('tareas/<int:pk>/tarea_confirm_delete', views.TareaDeleteView.as_view(), name='borrar tarea'),
    path('clientes/', views.ClienteListView.as_view(), name='index clientes'),
    path('clientes/reg_cliente', views.ClienteCreateView.as_view(), name='registrar cliente'),
    path('clientes/<int:pk>', views.ClienteDetailView.as_view(), name='cliente'),
    path('empleados/', views.EmpleadoListView.as_view(), name='index empleados'),
    path('empleados/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
]
