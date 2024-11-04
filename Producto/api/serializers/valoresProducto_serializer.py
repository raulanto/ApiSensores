from Producto.models import ValoresProducto
from rest_framework import serializers

class ValoresProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoresProducto
        fields = ['id', 'nombre', 'valorMaximo', 'valorMinimo', 'producto']

class ValoresProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoresProducto
        fields = [ 'nombre', 'valorMaximo', 'valorMinimo']

class ValoresProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoresProducto
        fields = [ 'nombre', 'valorMaximo', 'valorMinimo']