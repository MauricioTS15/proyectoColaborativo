from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('proyectos/', views.ProyectoListView.as_view(), name='index proyectos'),
 path('proyectos/reg_proyecto', views.reg_proyecto, name='registrar proyecto'),
 path('proyectos/<int:proyecto_id>', views.show_proyecto, name='proyecto'),
 path('proyectos/<int:proyecto_id>/mod_proyecto', views.mod_proyecto, name='modificar proyecto'),
 path('tareas/', views.TareaListView.as_view(), name='index tareas'),
 path('tareas/reg_tarea', views.reg_tarea, name='registrar tarea'),
 path('tareas/<int:tarea_id>', views.show_tarea, name='tarea'),
 path('tareas/<int:tarea_id>/mod_tarea', views.mod_tarea, name='modificar tarea'),
 path('clientes/', views.ClienteListView.as_view(), name='index clientes'),
 path('clientes/<int:cliente_id>', views.show_cliente, name='cliente'),
 path('empleados/', views.EmpleadoListView.as_view(), name='index empleados'),
 path('empleados/<int:empleado_id>', views.show_empleado, name='empleado'),
]