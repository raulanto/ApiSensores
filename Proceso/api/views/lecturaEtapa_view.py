# lectura etapa view

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
)


from rest_framework.generics import CreateAPIView
from ..serializers.lecturaEtapa_serializer import LecturaEtapaSerializer,LecturaEtapaCreateSerializer
from Proceso.models.LecturaEtapa import LecturaEtapa
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio

# filtros
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class LecturaEtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = LecturaEtapa.objects.all()

    serializer_class =LecturaEtapaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['fkESeccionEquipoSensor','valor','fkEtapa']
    search_fields = ['valor','fkEtapa']

class LecturaEtapaCreateViewSet(CreateAPIView):
    queryset = LecturaEtapa.objects.all()
    serializer_class = LecturaEtapaCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Lectura creado"
        registrarCambio(self.request, instance, mensaje)