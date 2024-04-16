from django.db import models
from simple_history.models import HistoricalRecords

from Plantas.models import Planta
from Producto.models import Producto
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Equipo(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    fkplanta = models.ForeignKey(Planta, related_name='equipos', on_delete=models.CASCADE, blank=True, null=True)
    fkproducto = models.ForeignKey(Producto, related_name='equipos', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.nombre

class SeccionEquipo(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    fkequipo = models.ForeignKey(Equipo, related_name='secciones', on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    history = HistoricalRecords()
    def __str__(self):
        return self.nombre

class Sensores(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    matricula=models.CharField(max_length=50,default='souhdofus')
    history = HistoricalRecords()
    def __str__(self):
        return self.nombre

class SeccionEquipoSensor(TimeStampedModel):
    fkseccionEquipo = models.ForeignKey(SeccionEquipo, related_name='secciones', on_delete=models.CASCADE, blank=True, null=True)
    fksensor = models.ForeignKey(Sensores, related_name='sensores', on_delete=models.CASCADE, blank=True, null=True)

    history = HistoricalRecords()
    def __str__(self):
        return self.fkseccionEquipo.nombre