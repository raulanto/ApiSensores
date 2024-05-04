from Plantas.models import TimeStampedModel
from django.db import models
from .Estado import Estado
class Municipio(TimeStampedModel):
    nombre = models.CharField(max_length=100,unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre