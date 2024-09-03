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
from Equipo.models import SeccionEquipoSensor
from ..serializers.seccionEquipoSensor_serializer import SeccionEquipoSensorSerializer, \
    SeccionEquipoSensorCreateSerializer, SeccionEquipoSensorUpdateSerializer

from rest_framework import filters
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
class SeccionEquipoSemsorViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = SeccionEquipoSensor.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['fkseccionEquipo']
    serializer_class = SeccionEquipoSensorSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SeccionEquipoSensorUpdateSerializer
        response = super().update(request, *args, **kwargs)
        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Seccion Equipo Sensor actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class SeccionEquipoSensorCreateAPIView(CreateAPIView):
    queryset = SeccionEquipoSensor.objects.all().order_by('id')
    serializer_class = SeccionEquipoSensorCreateSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Seccion equipo Sensor creado"
        registrarCambio(self.request, instance, mensaje)