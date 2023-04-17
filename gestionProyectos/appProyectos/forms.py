from django import forms

#formulario con campos de la clase proyecto
class ProyectoForm(forms.Form):
  clientes = [('1', 'pito cruzeta'),
              ]
  responsables = [('1', 'yuan cruzeta')
                  ]
  lista_tareas = [('1', 'ordenar estanterías'),
            ]
  
  nombre = forms.CharField(label='Nombre:', max_length=50, required=False)
  descripcion = forms.CharField(label='Descripción:', widget=forms.Textarea, max_length=255, required=False)
  fecha_inicio = forms.DateField(label='Fecha de incio', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
  fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
  presupuesto = forms.CharField(label='Presupuesto:', max_length=50, required=False)
  cliente = forms.ChoiceField(label='Cliente:', choices=clientes)
  responsable = forms.ChoiceField(label='Responsable:', choices=responsables)
  tareas = forms.MultipleChoiceField(label='Tareas:', choices=lista_tareas, required=False)

#formulario con campos de la clase tarea
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
  descripcion = forms.CharField(label='Descripción:', widget=forms.Textarea, max_length=255, required=False)
  fecha_inicio = forms.DateField(label='Fecha de incio', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
  fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
  responsable = forms.ChoiceField(label='Responsable:', choices=responsables)
  prioridad = forms.ChoiceField(label='Nivel de prioridad:', choices=niveles)
  estado = forms.ChoiceField(label='Estado:', choices=estados)
  notas = forms.CharField(label='Notas adicionales:', widget=forms.Textarea, max_length=255, required=False)
