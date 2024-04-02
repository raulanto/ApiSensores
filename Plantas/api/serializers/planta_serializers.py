from rest_framework import serializers

from Plantas.models import Estado,Municipio,Planta


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre']

class MunicipioSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Municipio
        fields = ['id', 'nombre', 'estado']


# Planta
class PlantaSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer()

    class Meta:
        model = Planta
        fields = ['id', 'nombre', 'codigo_postal', 'calle', 'municipio', 'descripcion', 'usuario']


class PlantaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ['nombre', 'codigo_postal', 'calle',  'municipio', 'descripcion', 'usuario']


class PlantaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ['nombre', 'codigo_postal', 'calle', 'municipio', 'descripcion']