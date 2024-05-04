from Organizacion.models.Organizacion import Organizacion
from Plantas.models import TimeStampedModel
from django.db import models
from .Municipio import Municipio

from django.contrib.auth.models import User
class Planta(TimeStampedModel):
    nombre = models.CharField(max_length=50, blank=False, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.ForeignKey(Municipio,related_name='municipio', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(blank=True, null=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.nombre
