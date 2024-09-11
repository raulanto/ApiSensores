from rest_framework import serializers
from Proceso.models import Proceso
class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['id','nombre','descripcion','usuario','fkequipo']



class ProcesoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion','usuario','fkequipo']


class ProcesoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['nombre','descripcion']


class ProcesoFkequipo(serializers.ModelSerializer):
    class Meta:
        model=Proceso
        fields = ['fkequipo']

