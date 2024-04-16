from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Organizacion(TimeStampedModel):
    nombre = models.CharField(max_length=45,default='Organizacion')
    fkUsuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.TextField(max_length=250,default='Empresa de Acuicultura ')
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre