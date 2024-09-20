from django.db import models
from simple_history.models import HistoricalRecords
from django.utils import timezone


# Create your models here.
class TimeStampedModel(models.Model):
    # Guardar la fecha actual con zona horaria
    created_at = models.DateField(default=timezone.now)
    # Guardar la fecha y hora actual con zona horaria
    updated_at = models.DateTimeField(default=timezone.now)
    # Guardar solo la hora actual con zona horaria
    createdTime_at = models.TimeField(default=timezone.now)

    # Para rastrear el historial de cambios
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
