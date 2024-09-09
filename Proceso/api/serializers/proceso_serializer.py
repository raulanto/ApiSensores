from rest_framework import serializers
from Proceso.models import Proceso

class ProcesoSerializer(serializers.ModelSerializer):
    fkequipo_nombre=serializers.ReadOnlyField(source="fkequipo.nombre")
    class Meta:
        model=Proceso
        fields = ['id','nombre','descripcion','usuario','fkequipo','fkequipo_nombre']

      # Te odia maldita perralll


class ProcesoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion','usuario','fkequipo']


class ProcesoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion']
