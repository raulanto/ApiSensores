from rest_framework import serializers
from Equipo.models import SeccionEquipo

class SeccionEquipoSerializer(serializers.ModelSerializer):
    fkequipo_nombre = serializers.ReadOnlyField(source='fkequipo.nombre')

    class Meta:
        model = SeccionEquipo
        fields = ['id', 'nombre', 'fkequipo_nombre', 'descripcion']

class SeccionEquipoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeccionEquipo
        fields = [ 'nombre', 'fkequipo', 'descripcion']

class SeccionEquipoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeccionEquipo
        fields = [ 'nombre', 'descripcion']