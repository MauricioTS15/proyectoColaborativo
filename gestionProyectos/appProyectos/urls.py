from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('proyectos/', views.index_proyectos, name='index_proyectos'),
 path('clientes/', views.index_clientes, name='index_clientes'),
 path('proyectos/<int:proyecto_id>', views.show_proyecto, name='proyecto'),
 path('tareas/<int:tarea_id>', views.show_tarea, name='tarea'),
 path('clientes/<int:cliente_id>', views.show_cliente, name='cliente'),
]