from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
from ..serializers.lecturaEtapa_serializer import LecturaEtapaSerializer,LecturaEtapaCreateSerializer
from Proceso.models import LecturaEtapa
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio


class LecturaEtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = LecturaEtapa.objects.all()

    serializer_class =LecturaEtapaSerializer
    permission_classes = [IsAuthenticated]



class LecturaEtapaCreateViewSet(CreateAPIView):
    queryset = LecturaEtapa.objects.all()
    serializer_class = LecturaEtapaCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Lectura creado"
        registrarCambio(self.request, instance, mensaje)