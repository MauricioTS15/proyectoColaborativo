from django import forms
from django.forms import ModelForm
from .models import Proyecto, Tarea, Cliente, Empleado

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
        
class RegClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class RegEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

# fecha = forms.DateField(label='Fecha:', widget=forms.DateInput(attrs={'type': 'date'}), required=False) <- formato date
