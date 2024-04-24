from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Plantas.api.serializers import PlantaSerializer,PlantaCreateSerializer,PlantaUpdateSerializer
from Plantas.models import *
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
# filtros
from rest_framework import filters

class PlantaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Planta.objects.all()

    serializer_class = PlantaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['usuario']
    filter_backends = [filters.SearchFilter]

    def update(self, request, *args, **kwargs):
        self.serializer_class = PlantaUpdateSerializer
        response = super().update(request, *args, **kwargs)
        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Planta actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class PlantaCreateAPIView(CreateAPIView):
    queryset = Planta.objects.all().order_by('id')
    serializer_class = PlantaCreateSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "PLanta creado"
        registrarCambio(self.request, instance, mensaje)