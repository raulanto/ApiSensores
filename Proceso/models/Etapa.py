from .TimeStampedModel import TimeStampedModel
from django.db import models
from .Inconveniente import Inconveniente
from .Proceso import Proceso
from django.utils import timezone

# 1 activo 2 desactivado 3 Terminado

NOTIFICATION_TYPES = (
    (1, 'Activo'),
    (2, 'Desactivado'),
    (3, 'Terminado'),
    (4, 'Error'),
)


class Etapa(TimeStampedModel):
    nombre = models.CharField(max_length=50, default='Etapa',verbose_name='Etapa')
    fkProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=False, null=False,verbose_name='Proceso')

    duracion = models.DurationField(blank=True, null=True, verbose_name="Duración")
    activo = models.IntegerField( choices=NOTIFICATION_TYPES, default=2)
    proceso=models.IntegerField(default=0)
    def __str__(self):
        return self.nombre

    def frenar(self, descripcion, usuario):
        self.activo = False
        self.save()
        Inconveniente.objects.create(etapa=self, descripcion=descripcion, creado_por=usuario)

    def continuar(self, descripcion, usuario):
        self.activo = True
        self.save()
        Inconveniente.objects.create(etapa=self, descripcion=descripcion, creado_por=usuario)
