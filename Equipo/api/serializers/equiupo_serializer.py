from rest_framework import serializers
from Equipo.models import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    fkplanta_nombre = serializers.ReadOnlyField(source='fkplanta.nombre')
    fkproducto_nombre = serializers.ReadOnlyField(source='fkproducto.nombre')

    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion',  'fkplanta_nombre', 'fkproducto_nombre']


class EquipoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion','fkplanta','fkproducto']

class EquipoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'descripcion','fkproducto']