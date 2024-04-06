from rest_framework import serializers
from Proceso.models import LecturaEtapa






# class LecturaEtapa(TimeStampedModel):
#     valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
#                                 verbose_name="Valor")
#     fkEtapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank=True, null=True)
#     fkESeccionEquipoSensor = models.ForeignKey(SeccionEquipoSensor, on_delete=models.CASCADE, blank=True, null=True)
#
#     history = HistoricalRecords()
#
#     def __str__(self):
#         return self.fkESeccionEquipoSensor.fkseccionEquipo.nombre

class LecturaEtapaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = LecturaEtapa
        fields=['id','valor','fkEtapa','fkESeccionEquipoSensor','created_at']


class LecturaEtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaEtapa
        fields = ['valor', 'fkEtapa','fkESeccionEquipoSensor']