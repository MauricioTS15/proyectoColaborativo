from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nivel_prioridad = models.CharField(max_length=50)
    estado_tarea = models.CharField(max_length=50)
    notas_adicionales = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarea_realizar = models.ManyToManyField(Tarea)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    