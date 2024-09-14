from .TimeStampedModel import TimeStampedModel
from django.db import models
from .Inconveniente import Inconveniente
from .Proceso import Proceso
from django.utils import timezone

# 1 activo 2 desactivado 3 Terminado


class Etapa(TimeStampedModel):
    nombre = models.CharField(max_length=50, default='Etapa',verbose_name='Etapa')
    # fkestadoEtapa = models.ForeignKey(EstadoEtapa, on_delete=models.CASCADE, blank=True, null=True)
    fkProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=False, null=False,verbose_name='Proceso')
    # duracion_en_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
    #                                         verbose_name="Duración en horas")
    duracion = models.DurationField(blank=True, null=True, verbose_name="Duración")
    activo = models.IntegerField(default=2)
    # fecha_inicio = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de inicio")

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

    # def save(self, *args, **kwargs):
    #     if self.activo and not self.fecha_inicio:
    #         self.fecha_inicio = timezone.now()
    #     super(Etapa, self).save(*args, **kwargs)