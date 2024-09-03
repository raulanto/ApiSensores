from rest_framework import serializers

from Producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'usuario',"fotografia"]


class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'usuario']


class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']
