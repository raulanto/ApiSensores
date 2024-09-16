# lectura etapa serializer

from rest_framework import serializers
from Proceso.models import LecturaEtapa
from Equipo.api.serializers import SeccionEquipoSensorSerializer


MONTH_NAMES = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

class LecturaEtapaSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    createdTime_at = serializers.TimeField(format='%H:%M:%S')
    fkESeccionEquipoSensor=SeccionEquipoSensorSerializer()
    class Meta:
        model = LecturaEtapa
        fields = ['id', 'valor', 'fkEtapa', 'fkESeccionEquipoSensor', 'created_at', 'createdTime_at']


    # Funcion que devuelve el mes en que se creo la lectura
    def get_created_at(self, obj):
        return MONTH_NAMES[obj.created_at.month - 1]



class LecturaEtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaEtapa
        fields = ['valor', 'fkEtapa','fkESeccionEquipoSensor']