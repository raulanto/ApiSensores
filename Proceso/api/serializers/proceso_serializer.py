from rest_framework import serializers
from Proceso.models import Proceso
class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['id','nombre','descripcion','usuario','equipo']

      # Te odia maldita perralll


class ProcesoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion','usuario','equipo']


class ProcesoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion']
