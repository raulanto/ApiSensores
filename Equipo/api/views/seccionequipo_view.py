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
from Equipo.models import SeccionEquipo
from ..serializers.seccionEquipo_serializer import SeccionEquipoSerializer,SeccionEquipoCreateSerializer,SeccionEquipoUpdateSerializer

from ApiSensores.registroCambios import registrarCambio

from rest_framework import filters

class SeccionEquipoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = SeccionEquipo.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['fkequipo']
    serializer_class = SeccionEquipoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SeccionEquipoUpdateSerializer
        response= super().update(request, *args, **kwargs)

        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Seccion Equipo actualizado"
        registrarCambio(request, objeto, mensaje)

        return response



class SeccionEquipoCreateAPIView(CreateAPIView):
    queryset = SeccionEquipo.objects.all().order_by('id')
    serializer_class = SeccionEquipoCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Seccion Equipo creado"
        registrarCambio(self.request, instance, mensaje)
