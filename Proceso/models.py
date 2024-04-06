from django.db import models
from simple_history.models import HistoricalRecords

from Equipo.models import Equipo
from django.contrib.auth.models import User
from Equipo.models import SeccionEquipoSensor


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Proceo control
class Proceso(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    equipo = models.ForeignKey(Equipo, related_name='procesos', on_delete=models.CASCADE, blank=True, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.nombre


class EstadoEtapa(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.nombre


class Etapa(TimeStampedModel):
    nombre = models.CharField(max_length=50,default='Etapa')
    fkestadoEtapa = models.ForeignKey(EstadoEtapa, on_delete=models.CASCADE, blank=True, null=True)
    fkProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=True, null=True)
    duracion_en_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                            verbose_name="Duración en horas")

    history = HistoricalRecords()

    def __str__(self):
        return self.nombre


class LecturaEtapa(TimeStampedModel):
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                verbose_name="Valor")
    fkEtapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank=True, null=True)
    fkESeccionEquipoSensor = models.ForeignKey(SeccionEquipoSensor, on_delete=models.CASCADE, blank=True, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.fkESeccionEquipoSensor.fkseccionEquipo.nombre
