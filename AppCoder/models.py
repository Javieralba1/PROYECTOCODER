import email
from xmlrpc.client import boolean
from django.db import models
from django.forms import BooleanField

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
class Entregable(models.Model):
     nombre = models.CharField(max_length=30)
     fechadeentrega= models.DateField()
     entregado = BooleanField()