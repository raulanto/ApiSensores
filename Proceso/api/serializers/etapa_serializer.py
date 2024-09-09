from rest_framework import serializers
from Proceso.models import Etapa

class EtapaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etapa
        fields= ['id','nombre','activo','fkProceso','duracion']

class EtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['activo','nombre','fkProceso','duracion']

class EtapaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['duracion']