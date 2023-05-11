from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Proyecto, Tarea, Cliente, Empleado

# formulario con campos de la clase proyecto
class ProyectoForm(ModelForm):
    descripcion = forms.CharField(label='Descripción:', widget=forms.Textarea(attrs={"rows":"5"}), required=False)
    fecha_inicio = forms.DateField(label='Fecha de inicio:', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(label='Fecha de fin:', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Proyecto
        fields = '__all__'

# formulario con campos de la clase tarea
class TareaForm(ModelForm):
    descripcion = forms.CharField(label='Descripción:', widget=forms.Textarea(attrs={"rows":"5"}), required=False)
    fecha_inicio = forms.DateField(label='Fecha de inicio:', widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(label='Fecha de fin:', widget=forms.DateInput(attrs={'type': 'date'}))
    notas = forms.CharField(label='Notas adicionales:', widget=forms.Textarea(attrs={"rows":"3"}), required=False)

    class Meta:
        model = Tarea
        fields = '__all__'
        
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Introduce tu nombre de usuario", max_length=155, required=True)
    password = forms.CharField(label="Introduce tu contraseña", max_length=155, required=True, widget=forms.PasswordInput)