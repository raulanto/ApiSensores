from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Equipo.api.serializers.equiupo_serializer import EquipoSerializer, EquipoCreateSerializer, EquipoUpdateSerializer
from Equipo.models import Equipo

# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
# filtros
from rest_framework import filters

class EquipoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Equipo.objects.all()

    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['nombre']
    search_fields = ['nombre']


    def update(self, request, *args, **kwargs):
        self.serializer_class = EquipoUpdateSerializer
        response =super().update(request, *args, **kwargs)
        # Registra el cambio
        objeto = self.get_object()
        mensaje = "equipo Actulizado actualizado"
        registrarCambio(request, objeto, mensaje)

        return response

class EquipoCreateAPIView(CreateAPIView):
    queryset = Equipo.objects.all().order_by('id')
    serializer_class = EquipoCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Equipo creado"
        registrarCambio(self.request, instance, mensaje)