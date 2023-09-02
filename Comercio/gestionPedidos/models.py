from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=150,verbose_name="Direccion envio")
    email=models.EmailField(blank=True, null=True) #Esto se pone para que en el panel administracion el mail no sea un campo requerido
    telefono=models.CharField(max_length=9)

class Articulos (models.Model):
    nombre=models.CharField(max_length=200)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()

class Pedidos (models.Model):
    numero=models.IntegerField()
    fecha=models.DateTimeField()
    entregado=models.BooleanField()