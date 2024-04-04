from rest_framework import serializers
from Proceso.models import EstadoEtapa

class EstadoEtapaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoEtapa
        fields= ['id','nombre','usuario']


class EstadoEtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEtapa
        fields = ['nombre', 'usuario']


class EstadoEtapaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoEtapa
        fields = ['nombre']