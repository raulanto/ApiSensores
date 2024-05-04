from .TimeStampedModel import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User

class EstadoEtapa(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.nombre
