from .TimeStampedModel import TimeStampedModel
from django.db import models
from .Inconveniente import Inconveniente
from .Proceso import Proceso


class Etapa(TimeStampedModel):
    nombre = models.CharField(max_length=50, default='Etapa',verbose_name='Etapa')
    # fkestadoEtapa = models.ForeignKey(EstadoEtapa, on_delete=models.CASCADE, blank=True, null=True)
    fkProceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, blank=False, null=False,verbose_name='Proceso')
    # duracion_en_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
    #                                         verbose_name="Duración en horas")
    duracion = models.DurationField(blank=True, null=True, verbose_name="Duración")
    activo = models.BooleanField(default=True)
    

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