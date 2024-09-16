from rest_framework import serializers
from Proceso.models import Etapa
from ..serializers.proceso_serializer import ProcesoFkequipo

class EtapaSerializer(serializers.ModelSerializer):
    fkProceso = ProcesoFkequipo()
    class Meta:
        model = Etapa
        fields= ['id','nombre','activo','fkProceso','duracion','created_at','createdTime_at','updated_at','proceso']

class EtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['activo','nombre','fkProceso','duracion']

class EtapaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['activo','proceso']