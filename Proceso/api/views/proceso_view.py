from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
from ..serializers.proceso_serializer import ProcesoUpdateSerializer,ProcesoCreateSerializer,ProcesoSerializer
from Proceso.models import Proceso
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
class ProcesoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Proceso.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['fkequipo','usuario']
    search_fields = ['nombre']

    serializer_class = ProcesoSerializer
    permission_classes = [IsAuthenticated]


    def update(self, request, *args, **kwargs):
        self.serializer_class = ProcesoUpdateSerializer
        response = super().update(request, *args, **kwargs)


        # Registra el cambio
        objeto = self.get_object()
        mensaje = "Proceso actualizado"
        registrarCambio(request, objeto, mensaje)

        return response

class ProcesoCreateViewSet(CreateAPIView):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Proceso creado"
        registrarCambio(self.request, instance, mensaje)
