from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    Email_usuario = models.EmailField()
    Edad = models.IntegerField(blank=True, null=True)
    Conexion = models.TextField(blank=True)
