
from Equipo.models import TimeStampedModel, SeccionEquipo


from django.db import models

from Equipo.models.Sensores import Sensores


class SeccionEquipoSensor(TimeStampedModel):
    fkseccionEquipo = models.ForeignKey(SeccionEquipo, related_name='secciones', on_delete=models.CASCADE)
    fksensor = models.ForeignKey(Sensores, related_name='sensor', on_delete=models.CASCADE)

    def __str__(self):
        return self.fkseccionEquipo.nombre