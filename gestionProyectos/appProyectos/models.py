from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=155)
    apellido = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=155)
    apellido = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Prioridad(models.Model):
    nombre = models.CharField(max_length=155)
    
    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    nombre = models.CharField(max_length=155)
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=155)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    notas = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=155)
    descripcion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tareas = models.ManyToManyField(Tarea)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    