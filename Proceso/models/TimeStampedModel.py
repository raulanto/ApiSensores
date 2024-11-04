from django.db import models
from simple_history.models import HistoricalRecords
from django.utils import timezone


# Create your models here.
class TimeStampedModel(models.Model):
    # Guardar la fecha actual (solo al crear)
    created_at = models.DateField(auto_now_add=True)
    # Actualizar automáticamente la fecha y hora cada vez que se guarda
    updated_at = models.DateTimeField(auto_now=True)
    # Guardar solo la hora actual al crear
    createdTime_at = models.TimeField(auto_now_add=True)

    # Para rastrear el historial de cambios
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
