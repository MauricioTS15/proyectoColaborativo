from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()
class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nivel_prioridad = models.CharField(max_length=50)
    estado_tarea = models.CharField(max_length=50)
    notas_adicionales = models.CharField(max_length=50)
class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarea_realizar = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    

    