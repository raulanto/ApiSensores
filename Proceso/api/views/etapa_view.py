from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Proceso.models import Etapa
from ..serializers.etapa_serializer import EtapaCreateSerializer, EtapaUpdateSerializer, EtapaSerializer
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class EtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Etapa.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['id','fkProceso']
    serializer_class = EtapaSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = EtapaUpdateSerializer
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Etapa actualizado"
        registrarCambio(request, objeto, mensaje)

        return response

class EtapaCreateViewSet(CreateAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Etapa creado"
        registrarCambio(self.request, instance, mensaje)