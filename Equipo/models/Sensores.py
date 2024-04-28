from Equipo.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import User

class Sensores(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    matricula=models.CharField(max_length=10,default='VVFYGIYFCIUY')

    def __str__(self):
        return self.nombre