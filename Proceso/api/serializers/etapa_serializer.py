from rest_framework import serializers
from Proceso.models import Etapa

class EtapaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etapa
        fields= ['id','nombre','fkestadoEtapa','fkProceso','duracion_en_horas']

class EtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['fkestadoEtapa','nombre','fkProceso','duracion_en_horas']

class EtapaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['duracion_en_horas']