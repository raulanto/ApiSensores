from .TimeStampedModel import TimeStampedModel
from django.db import models
from simple_history.models import HistoricalRecords
from .EstadoEtapa import EstadoEtapa
from .Proceso import Proceso
class Etapa(TimeStampedModel):
    nombre = models.CharField(max_length=50,default='Etapa')
    fkestadoEtapa = models.ForeignKey(EstadoEtapa, on_delete=models.CASCADE, blank=True, null=True)
    fkProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=True, null=True)
    duracion_en_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                            verbose_name="Duración en horas")


    def __str__(self):
        return self.nombre
