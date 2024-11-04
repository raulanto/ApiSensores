from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView


from Producto.models import ValoresProducto

from ..serializers import ValoresProductoCreateSerializer, ValoresProductoUpdateSerializer, ValoresProductoSerializer
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio


class ValoresProductoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = ValoresProducto.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['producto']
    serializer_class = ValoresProductoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = ValoresProductoUpdateSerializer
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "ValoresProducto actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class ValoresProductoCreateViewSet(CreateAPIView):
    queryset = ValoresProducto.objects.all()
    serializer_class = ValoresProductoCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "ValoresProducto creado"
        registrarCambio(self.request, instance, mensaje)
