from django.db import models
from .TimeStampedModel import TimeStampedModel
from Equipo.models import Equipo
from django.contrib.auth.models import User

class Proceso(TimeStampedModel):
    nombre = models.CharField(max_length=50,verbose_name='Proceso')
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fkequipo = models.ForeignKey(Equipo, related_name='procesos', on_delete=models.CASCADE, blank=True, null=True,verbose_name='Equipo')

    def __str__(self):
        return self.nombre