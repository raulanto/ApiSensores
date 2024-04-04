from rest_framework import serializers
from Equipo.models import SeccionEquipoSensor

class SeccionEquipoSensorSerializer(serializers.ModelSerializer):
    fkseccionEquipo_nombre = serializers.ReadOnlyField(source='fkseccionEquipo.nombre')
    fksensor_nombre = serializers.ReadOnlyField(source='fksensor.nombre')

    class Meta:
        model = SeccionEquipoSensor
        fields = ['id',  'fkseccionEquipo_nombre', 'fksensor_nombre']

class SeccionEquipoSensorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeccionEquipoSensor
        fields = ['fkseccionEquipo', 'fksensor']


class SeccionEquipoSensorUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeccionEquipoSensor
        fields = ['fkseccionEquipo', 'fksensor']