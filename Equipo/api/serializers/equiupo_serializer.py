from rest_framework import serializers
from Equipo.models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    fkplanta_nombre = serializers.ReadOnlyField(source='fkplanta.nombre')
    fkproducto_nombre = serializers.ReadOnlyField(source='fkproducto.nombre')
    # fkplanta_organizacion= serializers.ReadOnlyField(source='fkplanta.organizacion')
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion',  'fkplanta_nombre', 'fkproducto_nombre','usuario']


class EquipoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion','fkplanta','fkproducto','usuario']

class EquipoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion','fkproducto']