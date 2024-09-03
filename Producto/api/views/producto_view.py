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

from Producto.models import Producto

from ..serializers import (ProductoCreateSerializer,ProductoSerializer,ProductoUpdateSerializer)
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio

class ProductoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Producto.objects.all()

    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['usuario']

    def update(self, request, *args, **kwargs):
        self.serializer_class = ProductoUpdateSerializer
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Producto actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class ProductoCreateViewSet(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Producto creado"
        registrarCambio(self.request, instance, mensaje)
