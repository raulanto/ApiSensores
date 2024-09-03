from rest_framework import serializers
from Equipo.models import Sensores


class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = ['id', 'nombre','usuario','matricula']


class SensoresCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = ['nombre','usuario']

class SensoresUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = ['nombre']