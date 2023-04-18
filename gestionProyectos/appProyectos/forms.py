from django import forms
from django.forms import ModelForm
from .models import Proyecto, Tarea

# formulario con campos de la clase proyecto


class RegProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

# formulario con campos de la clase tarea


class RegTareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

# fecha = forms.DateField(label='Fecha:', widget=forms.DateInput(attrs={'type': 'date'}), required=False) <- formato date
