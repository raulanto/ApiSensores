# clase lectura etapa

from .TimeStampedModel import TimeStampedModel
from django.db import models
from simple_history.models import HistoricalRecords
from Equipo.models.SeccionEquipoSensor import SeccionEquipoSensor
from .Etapa import Etapa

class LecturaEtapa(TimeStampedModel):
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                verbose_name="Valor")
    fkEtapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank=True, null=True)
    fkESeccionEquipoSensor = models.ForeignKey(SeccionEquipoSensor, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.fkESeccionEquipoSensor.fkseccionEquipo.nombre