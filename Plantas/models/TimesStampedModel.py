from django.db import models
from simple_history.models import HistoricalRecords

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)
    class Meta:
        abstract = True