from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from Organizacion.models import Organizacion

# Control de cambios de los modelos
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Estado(TimeStampedModel):
    nombre = models.CharField(max_length=100,unique=True)

    history = HistoricalRecords()
    def __str__(self):
       return self.nombre



class Municipio(TimeStampedModel):
    nombre = models.CharField(max_length=100,unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    history = HistoricalRecords()
    def __str__(self):
        return self.nombre


class Planta(TimeStampedModel):
    nombre = models.CharField(max_length=50, blank=False, default='Planta', null=True,unique=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.ForeignKey(Municipio,related_name='municipio', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank=True, null=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, blank=True, null=True)


    history = HistoricalRecords()
    def __str__(self):
        return self.nombre
