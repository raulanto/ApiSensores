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

# Creamos uno para history
class EquipoHistorySerializer(serializers.ModelSerializer):
    history_id = serializers.ReadOnlyField()
    history_user = serializers.StringRelatedField()
    history_date = serializers.DateTimeField()
    history_type = serializers.CharField()  #: + (creado), ~ (modificado), - (eliminado)
    # se usa para para indexar el metodo
    # history_type = serializers.SerializerMethodField()  # Usaremos un método para traducir el símbolo
    class Meta:
        model = Equipo.history.model  # Acceso al modelo de historial
        fields = ['history_id', 'history_user', 'history_date', 'history_type', 'nombre', 'descripcion', 'fkplanta', 'fkproducto', 'usuario']

    # Retorna la palabra
    # def get_history_type(self, obj):
    #     # Traducir el tipo de cambio a texto legible
    #     type_mapping = {
    #         "+": "Creación",
    #         "~": "Modificación",
    #         "-": "Eliminación"
    #     }
    #     return type_mapping.get(obj.history_type, "Desconocido")