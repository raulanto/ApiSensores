from rest_framework import serializers
from Proceso.models import Etapa
from ..serializers.proceso_serializer import ProcesoFkequipo

from rest_framework import serializers
from django.utils import timezone

class EtapaSerializer(serializers.ModelSerializer):
    fkProceso = ProcesoFkequipo()

    # Sobrescribir el campo createdTime_at para devolver la hora en formato deseado
    createdTime_at = serializers.SerializerMethodField()

    class Meta:
        model = Etapa
        fields = ['id', 'nombre', 'activo', 'fkProceso', 'duracion', 'created_at', 'createdTime_at', 'updated_at', 'proceso']

    def get_createdTime_at(self, obj):
        # Formatear la hora en el formato 08:08:50
        return obj.createdTime_at.strftime('%H:%M:%S')


class EtapaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['activo','nombre','fkProceso','duracion']

class EtapaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields= ['activo','proceso']