from django.db import models

from Plantas.models import TimeStampedModel


class Estado(TimeStampedModel):
    nombre = models.CharField(max_length=100,unique=True)
    def __str__(self):
       return self.nombre
