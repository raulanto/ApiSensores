from django.db import models
from .TimeStampedModel import TimeStampedModel
from Equipo.models import Equipo
from django.contrib.auth.models import User

class Proceso(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    equipo = models.ForeignKey(Equipo, related_name='procesos', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre