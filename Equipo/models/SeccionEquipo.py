from django.db import models
from Equipo.models import TimeStampedModel,Equipo

class SeccionEquipo(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    fkequipo = models.ForeignKey(Equipo, related_name='secciones', on_delete=models.CASCADE, blank=True, null=True ,verbose_name='Equipo')
    descripcion = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nombre
