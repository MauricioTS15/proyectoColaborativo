from django import forms
from django.forms import ModelForm
from .models import Proyecto

# formulario con campos de la clase proyecto
class RegProyecto(ModelForm):
  
  class Meta:
    model = Proyecto
    fields = '__all__'

# formulario con campos de la clase tarea


class TareaForm(forms.Form):
    responsables = [('1', 'yuan cruzeta')
                    ]
    niveles = [('Alta', 'Alta'),
               ('Media', 'Media'),
               ('Baja', 'Baja')
               ]
    estados = [('Abierta', 'Abierta'),
               ('Asignada', 'Asignada'),
               ('En proceso', 'En proceso'),
               ('Finalizada', 'Finalizada')
               ]

    nombre = forms.CharField(label='Nombre:', max_length=50, required=False)
    descripcion = forms.CharField(
        label='Descripción:', widget=forms.Textarea, max_length=255, required=False)
    fecha_inicio = forms.DateField(label='Fecha de incio', widget=forms.DateInput(
        attrs={'type': 'date'}), required=False)
    fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(
        attrs={'type': 'date'}), required=False)
    responsable = forms.ChoiceField(label='Responsable:', choices=responsables)
    prioridad = forms.ChoiceField(label='Nivel de prioridad:', choices=niveles)
    estado = forms.ChoiceField(label='Estado:', choices=estados)
    notas = forms.CharField(label='Notas adicionales:',
                            widget=forms.Textarea, max_length=255, required=False)
