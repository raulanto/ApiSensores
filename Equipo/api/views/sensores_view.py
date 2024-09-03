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
from Equipo.models import Sensores
from ..serializers import SensoresSerializer, SensoresCreateSerializer, SensoresUpdateSerializer
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
from rest_framework import filters
class SensoresViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Sensores.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['nombre','usuario']
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SensoresUpdateSerializer
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Sensores actualizado"
        registrarCambio(request, objeto, mensaje)

        return response


class SensoresCreateAPIView(CreateAPIView):
    queryset = Sensores.objects.all().order_by('id')
    serializer_class = SensoresCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Sensores creado"
        registrarCambio(self.request, instance, mensaje)