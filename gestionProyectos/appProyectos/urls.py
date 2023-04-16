from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('proyectos/', views.index_proyectos, name='index proyectos'),
 path('proyectos/reg_proyecto', views.reg_proyecto, name='registrar proyecto'),
 path('proyectos/<int:proyecto_id>', views.show_proyecto, name='proyecto'),
 path('proyectos/<int:proyecto_id>/mod_proyecto', views.mod_proyecto, name='modificar proyecto'),
 path('tareas/', views.index_tareas, name='index tareas'),
 path('tareas/reg_tarea', views.reg_tarea, name='registrar tarea'),
 path('tareas/<int:tarea_id>', views.show_tarea, name='tarea'),
 path('tareas/<int:tarea_id>/mod_tarea', views.mod_tarea, name='modificar tarea'),
 path('clientes/', views.index_clientes, name='index clientes'),
 path('clientes/<int:cliente_id>', views.show_cliente, name='cliente'),
 path('empleados/', views.index_empleados, name='index empleados'),
 path('empleados/<int:empleado_id>', views.show_empleado, name='empleado'),
]