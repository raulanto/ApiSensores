from django.db import models
from django.contrib.auth.models import User

from Equipo.models import TimeStampedModel
from Plantas.models import Planta
from Producto.models import Producto

class Equipo(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    fkplanta = models.ForeignKey(Planta, related_name='equipos', on_delete=models.CASCADE, blank=True, null=True)
    fkproducto = models.ForeignKey(Producto, related_name='equipos', on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(User,related_name='usuario', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre