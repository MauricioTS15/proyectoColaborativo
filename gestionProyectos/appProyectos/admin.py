from django.contrib import admin
from .models import Cliente, Empleado, Prioridad, Estado, Tarea, Proyecto
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Prioridad)
admin.site.register(Estado)
admin.site.register(Tarea)
admin.site.register(Proyecto)