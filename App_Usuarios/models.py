from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni= models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    fecha_de_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}- {self.dni} años)" 
    
class Proveedor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni= models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    servicio_proveedor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}- {self.servicio_proveedor})" 


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - ${self.stock}"
# Create your models here.
