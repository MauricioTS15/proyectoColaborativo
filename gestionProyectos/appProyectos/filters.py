import django_filters
from django import forms
from .models import Proyecto, Tarea, Cliente, Empleado

class ProyectoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(label='Nombre:', lookup_expr='icontains')
    fecha_inicio = django_filters.DateFilter(label='Fecha de inicio:', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = django_filters.DateFilter(label='Fecha de fin:', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Proyecto
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'presupuesto', 'cliente', 'responsable']
        