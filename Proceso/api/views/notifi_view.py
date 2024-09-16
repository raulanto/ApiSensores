from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Modelo y seri
from Proceso.models import Notificacion
from ..serializers import NotificacionSerializers,NotificacionCreateSerializers,NotificacionUpdateSerializers


class NotificacionViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Notificacion.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['id','user','is_read']
    serializer_class = NotificacionSerializers
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = NotificacionUpdateSerializers
        response = super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Notificacion  actualizado"
        registrarCambio(request, objeto, mensaje)

        return response

class NotificacionCreateViewSet(CreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionCreateSerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Notificacion creado"
        registrarCambio(self.request, instance, mensaje)